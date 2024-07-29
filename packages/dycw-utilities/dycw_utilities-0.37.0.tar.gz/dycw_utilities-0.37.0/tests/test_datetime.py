from __future__ import annotations

import datetime as dt
from math import isclose
from operator import eq, gt, lt
from re import search
from typing import TYPE_CHECKING, Any
from zoneinfo import ZoneInfo

from hypothesis import HealthCheck, assume, given, settings
from hypothesis.strategies import (
    DataObject,
    SearchStrategy,
    data,
    dates,
    datetimes,
    floats,
    integers,
    just,
    sampled_from,
    timedeltas,
    times,
    timezones,
)
from pytest import mark, param, raises

from utilities.datetime import (
    DAY,
    EPOCH_UTC,
    HOUR,
    MINUTE,
    MONTH,
    NOW_HK,
    NOW_TOKYO,
    NOW_UTC,
    QUARTER,
    SECOND,
    TODAY_HK,
    TODAY_TOKYO,
    TODAY_UTC,
    WEEK,
    YEAR,
    AddWeekdaysError,
    FormatDatetimeLocalAndUTCError,
    Month,
    MonthError,
    ParseDateError,
    ParseDateTimeError,
    ParseMonthError,
    ParseTimedeltaError,
    ParseTimeError,
    YieldDaysError,
    YieldWeekdaysError,
    add_weekdays,
    date_to_datetime,
    date_to_month,
    duration_to_float,
    duration_to_timedelta,
    ensure_date,
    ensure_datetime,
    ensure_month,
    ensure_time,
    ensure_timedelta,
    format_datetime_local_and_utc,
    get_months,
    get_now,
    get_now_hk,
    get_now_tokyo,
    get_quarters,
    get_today,
    get_today_hk,
    get_today_tokyo,
    get_years,
    is_equal_mod_tz,
    is_weekday,
    maybe_sub_pct_y,
    parse_date,
    parse_datetime,
    parse_month,
    parse_time,
    parse_timedelta,
    round_to_next_weekday,
    round_to_prev_weekday,
    serialize_date,
    serialize_datetime,
    serialize_month,
    serialize_time,
    serialize_timedelta,
    yield_days,
    yield_weekdays,
)
from utilities.hypothesis import assume_does_not_raise, months, text_clean
from utilities.types import ensure_class
from utilities.zoneinfo import HONG_KONG, TOKYO, UTC

if TYPE_CHECKING:
    from collections.abc import Callable

    from utilities.types import Number


class TestAddWeekdays:
    @given(date=dates(), n=integers(-10, 10))
    @mark.parametrize("predicate", [param(gt), param(lt)])
    def test_add(
        self, *, date: dt.date, n: int, predicate: Callable[[Any, Any], bool]
    ) -> None:
        _ = assume(predicate(n, 0))
        with assume_does_not_raise(OverflowError):
            result = add_weekdays(date, n=n)
        assert is_weekday(result)
        assert predicate(result, date)

    @given(date=dates())
    def test_zero(self, *, date: dt.date) -> None:
        _ = assume(is_weekday(date))
        result = add_weekdays(date, n=0)
        assert result == date

    @given(date=dates())
    @settings(suppress_health_check={HealthCheck.filter_too_much})
    def test_error(self, *, date: dt.date) -> None:
        _ = assume(not is_weekday(date))
        with raises(AddWeekdaysError):
            _ = add_weekdays(date, n=0)

    @given(date=dates(), n1=integers(-10, 10), n2=integers(-10, 10))
    def test_two(self, *, date: dt.date, n1: int, n2: int) -> None:
        with assume_does_not_raise(AddWeekdaysError, OverflowError):
            weekday1, weekday2 = (add_weekdays(date, n=n) for n in [n1, n2])
        result = weekday1 <= weekday2
        expected = n1 <= n2
        assert result is expected


class TestDateToDatetime:
    @given(date=dates())
    def test_main(self, *, date: dt.date) -> None:
        result = date_to_datetime(date).date()
        assert result == date


class TestDateToMonth:
    @given(date=dates())
    def test_main(self, *, date: dt.date) -> None:
        result = date_to_month(date).to_date(day=date.day)
        assert result == date


class TestDurationToFloat:
    @given(duration=integers(0, 10) | floats(0.0, 10.0))
    def test_number(self, *, duration: Number) -> None:
        result = duration_to_float(duration)
        assert result == duration

    @given(duration=timedeltas())
    def test_timedelta(self, *, duration: dt.timedelta) -> None:
        result = duration_to_float(duration)
        assert result == duration.total_seconds()


class TestDurationToTimedelta:
    @given(duration=integers(0, 10))
    def test_int(self, *, duration: int) -> None:
        result = duration_to_timedelta(duration)
        assert result.total_seconds() == duration

    @given(duration=floats(0.0, 10.0))
    def test_float(self, *, duration: float) -> None:
        duration = round(10 * duration) / 10
        result = duration_to_timedelta(duration)
        assert isclose(result.total_seconds(), duration)

    @given(duration=timedeltas())
    def test_timedelta(self, *, duration: dt.timedelta) -> None:
        result = duration_to_timedelta(duration)
        assert result == duration


class TestEnsure:
    @given(data=data())
    @mark.parametrize(
        ("strategy", "func"),
        [
            param(dates(), ensure_date),
            param(months(), ensure_month),
            param(times(), ensure_time),
            param(timedeltas(), ensure_timedelta),
        ],
    )
    def test_main(
        self,
        *,
        data: DataObject,
        strategy: SearchStrategy[Any],
        func: Callable[[Any], Any],
    ) -> None:
        value = data.draw(strategy)
        str_or_value = data.draw(sampled_from([value, str(value)]))
        result = func(str_or_value)
        assert result == value

    @given(data=data(), datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])))
    def test_datetime(self, *, data: DataObject, datetime: dt.datetime) -> None:
        datetime_or_str = data.draw(sampled_from([datetime, str(datetime)]))
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = ensure_datetime(datetime_or_str, time_zone=time_zone)
        assert result == datetime


class TestEpochUTC:
    def test_main(self) -> None:
        assert isinstance(EPOCH_UTC, dt.datetime)
        assert EPOCH_UTC.tzinfo is UTC


class TestFormatDatetimeLocalAndUTC:
    @mark.parametrize(
        ("datetime", "expected"),
        [
            param(
                dt.datetime(2000, 1, 1, 2, 3, 4, tzinfo=UTC),
                "2000-01-01 02:03:04 (Sat, UTC)",
            ),
            param(
                dt.datetime(2000, 1, 1, 2, 3, 4, tzinfo=HONG_KONG),
                "2000-01-01 02:03:04 (Sat, Asia/Hong_Kong, 1999-12-31 18:03:04 UTC)",
            ),
            param(
                dt.datetime(2000, 2, 1, 2, 3, 4, tzinfo=HONG_KONG),
                "2000-02-01 02:03:04 (Tue, Asia/Hong_Kong, 01-31 18:03:04 UTC)",
            ),
            param(
                dt.datetime(2000, 2, 2, 2, 3, 4, tzinfo=HONG_KONG),
                "2000-02-02 02:03:04 (Wed, Asia/Hong_Kong, 02-01 18:03:04 UTC)",
            ),
            param(
                dt.datetime(2000, 2, 2, 14, 3, 4, tzinfo=HONG_KONG),
                "2000-02-02 14:03:04 (Wed, Asia/Hong_Kong, 06:03:04 UTC)",
            ),
        ],
    )
    def test_main(self, *, datetime: dt.datetime, expected: str) -> None:
        result = format_datetime_local_and_utc(datetime)
        assert result == expected

    def test_error(self) -> None:
        datetime = dt.datetime(2000, 1, 1)  # noqa: DTZ001
        with raises(
            FormatDatetimeLocalAndUTCError,
            match="Datetime must have a time zone; got 2000-01-01 00:00:00",
        ):
            _ = format_datetime_local_and_utc(datetime)


class TestGetNow:
    @given(time_zone=timezones())
    def test_main(self, *, time_zone: ZoneInfo) -> None:
        now = get_now(time_zone=time_zone)
        assert isinstance(now, dt.datetime)
        assert now.tzinfo is time_zone

    def test_local(self) -> None:
        now = get_now(time_zone="local")
        assert isinstance(now, dt.datetime)
        ETC = ZoneInfo("Etc/UTC")  # noqa: N806
        assert now.tzinfo in {ETC, HONG_KONG, TOKYO, UTC}

    @mark.parametrize(
        "get_now", [param(get_now), param(get_now_hk), param(get_now_tokyo)]
    )
    def test_getters(self, *, get_now: Callable[[], dt.datetime]) -> None:
        assert isinstance(get_now(), dt.date)

    @mark.parametrize("now", [param(NOW_UTC), param(NOW_HK), param(NOW_TOKYO)])
    def test_constants(self, *, now: dt.datetime) -> None:
        assert isinstance(now, dt.date)


class TestGetTimedelta:
    @given(n=integers(-10, 10))
    @mark.parametrize(
        "get_timedelta", [param(get_months), param(get_quarters), param(get_years)]
    )
    def test_getters(
        self, *, get_timedelta: Callable[..., dt.timedelta], n: int
    ) -> None:
        assert isinstance(get_timedelta(n=n), dt.timedelta)

    @mark.parametrize("timedelta", [param(MONTH), param(QUARTER), param(YEAR)])
    def test_constants(self, *, timedelta: dt.timedelta) -> None:
        assert isinstance(timedelta, dt.timedelta)


class TestGetToday:
    @given(time_zone=timezones())
    def test_main(self, *, time_zone: ZoneInfo) -> None:
        today = get_today(time_zone=time_zone)
        assert isinstance(today, dt.date)

    @mark.parametrize(
        "get_today", [param(get_today), param(get_today_hk), param(get_today_tokyo)]
    )
    def test_getters(self, *, get_today: Callable[[], dt.datetime]) -> None:
        assert isinstance(get_today(), dt.date)

    @mark.parametrize("today", [param(TODAY_UTC), param(TODAY_HK), param(TODAY_TOKYO)])
    def test_constants(self, *, today: dt.date) -> None:
        assert isinstance(today, dt.date)


class TestIsEqualModTz:
    @given(x=datetimes(), y=datetimes())
    def test_naive(self, *, x: dt.datetime, y: dt.datetime) -> None:
        assert is_equal_mod_tz(x, y) == (x == y)

    @given(x=datetimes(timezones=just(UTC)), y=datetimes(timezones=just(UTC)))
    def test_utc(self, *, x: dt.datetime, y: dt.datetime) -> None:
        assert is_equal_mod_tz(x, y) == (x == y)

    @given(x=datetimes(), y=datetimes())
    def test_naive_vs_utc(self, *, x: dt.datetime, y: dt.datetime) -> None:
        expected = x == y
        naive = x
        aware = y.replace(tzinfo=UTC)
        assert is_equal_mod_tz(naive, aware) == expected
        assert is_equal_mod_tz(aware, naive) == expected


class TestIsWeekday:
    @given(date=dates())
    def test_main(self, *, date: dt.date) -> None:
        result = is_weekday(date)
        name = date.strftime("%A")
        expected = name in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
        assert result is expected


class TestMaybeSubPctY:
    @given(text=text_clean())
    def test_main(self, *, text: str) -> None:
        result = maybe_sub_pct_y(text)
        _ = assume(not search("%Y", result))
        assert not search("%Y", result)


class TestMonth:
    @mark.parametrize(
        ("month", "n", "expected"),
        [
            param(Month(2000, 1), -2, Month(1999, 11)),
            param(Month(2000, 1), -1, Month(1999, 12)),
            param(Month(2000, 1), 0, Month(2000, 1)),
            param(Month(2000, 1), 1, Month(2000, 2)),
            param(Month(2000, 1), 2, Month(2000, 3)),
            param(Month(2000, 1), 11, Month(2000, 12)),
            param(Month(2000, 1), 12, Month(2001, 1)),
        ],
    )
    def test_add(self, *, month: Month, n: int, expected: Month) -> None:
        result = month + n
        assert result == expected

    @given(month=months())
    def test_hashable(self, *, month: Month) -> None:
        _ = hash(month)

    @mark.parametrize("func", [param(repr), param(str)])
    def test_repr(self, *, func: Callable[..., str]) -> None:
        result = func(Month(2000, 12))
        expected = "2000-12"
        assert result == expected

    @mark.parametrize(
        ("month", "n", "expected"),
        [
            param(Month(2000, 1), -2, Month(2000, 3)),
            param(Month(2000, 1), -1, Month(2000, 2)),
            param(Month(2000, 1), 0, Month(2000, 1)),
            param(Month(2000, 1), 1, Month(1999, 12)),
            param(Month(2000, 1), 2, Month(1999, 11)),
            param(Month(2000, 1), 12, Month(1999, 1)),
            param(Month(2000, 1), 13, Month(1998, 12)),
        ],
    )
    def test_subtract(self, *, month: Month, n: int, expected: Month) -> None:
        result = month - n
        assert result == expected

    def test_to_date(self) -> None:
        result = Month(2000, 1).to_date(day=1)
        expected = dt.date(2000, 1, 1)
        assert result == expected

    def test_error(self) -> None:
        with raises(MonthError, match=r"Invalid year and month: \d+, \d+"):
            _ = Month(2000, 13)


class TestParseDate:
    @given(date=dates())
    def test_str(self, *, date: dt.date) -> None:
        result = parse_date(str(date))
        assert result == date

    @given(date=dates())
    def test_isoformat(self, *, date: dt.date) -> None:
        result = parse_date(date.isoformat())
        assert result == date

    @given(
        date=dates(),
        fmt=sampled_from(["%Y%m%d", "%Y %m %d", "%d%b%Y", "%d %b %Y"]).map(
            maybe_sub_pct_y
        ),
    )
    def test_various_formats(self, *, date: dt.date, fmt: str) -> None:
        result = parse_date(date.strftime(fmt))
        assert result == date

    def test_error(self) -> None:
        with raises(ParseDateError, match="Unable to parse date; got 'error'"):
            _ = parse_date("error")


class TestParseDateTime:
    @given(datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])))
    def test_str(self, *, datetime: dt.datetime) -> None:
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(str(datetime), time_zone=time_zone)
        assert result == datetime

    @given(datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])))
    def test_isoformat(self, *, datetime: dt.datetime) -> None:
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.isoformat(), time_zone=time_zone)
        assert result == datetime

    @given(
        datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])),
        fmt=sampled_from(["%Y%m%dT%H%M%S.%f%z", "%Y-%m-%d %H:%M:%S.%f%z"]).map(
            maybe_sub_pct_y
        ),
    )
    def test_yyyymmdd_hhmmss_fff_zzzz(self, *, datetime: dt.datetime, fmt: str) -> None:
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.strftime(fmt), time_zone=time_zone)
        assert result == datetime

    @given(
        datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])),
        fmt=sampled_from(["%Y%m%dT%H%M%S.%f", "%Y-%m-%d %H:%M:%S.%f"]).map(
            maybe_sub_pct_y
        ),
    )
    def test_yyyymmdd_hhmmss_fff(self, *, datetime: dt.datetime, fmt: str) -> None:
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.strftime(fmt), time_zone=time_zone)
        assert result == datetime

    @given(
        datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])),
        fmt=sampled_from([
            "%Y%m%dT%H%M%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%dT%H:%M:%S",
        ]).map(maybe_sub_pct_y),
    )
    def test_yyyymmdd_hhmmss(self, *, datetime: dt.datetime, fmt: str) -> None:
        datetime = datetime.replace(microsecond=0)
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.strftime(fmt), time_zone=time_zone)
        assert result == datetime

    @given(
        datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])),
        fmt=sampled_from(["%Y%m%dT%H%M", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M"]).map(
            maybe_sub_pct_y
        ),
    )
    def test_yyyymmdd_hhmm(self, *, datetime: dt.datetime, fmt: str) -> None:
        datetime = datetime.replace(second=0, microsecond=0)
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.strftime(fmt), time_zone=time_zone)
        assert result == datetime

    @given(
        datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])),
        fmt=sampled_from(["%Y%m%dT%H", "%Y-%m-%d %H", "%Y-%m-%dT%H"]).map(
            maybe_sub_pct_y
        ),
    )
    def test_yyyymmdd_hh(self, *, datetime: dt.datetime, fmt: str) -> None:
        datetime = datetime.replace(minute=0, second=0, microsecond=0)
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.strftime(fmt), time_zone=time_zone)
        assert result == datetime

    @given(
        datetime=datetimes(timezones=sampled_from([UTC, HONG_KONG])),
        fmt=sampled_from(["%Y%m%d", "%Y-%m-%d"]).map(maybe_sub_pct_y),
    )
    def test_yyyymmdd(self, *, datetime: dt.datetime, fmt: str) -> None:
        datetime = datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        time_zone = ensure_class(datetime.tzinfo, ZoneInfo)
        result = parse_datetime(datetime.strftime(fmt), time_zone=time_zone)
        assert result == datetime

    def test_error(self) -> None:
        with raises(ParseDateTimeError, match="Unable to parse datetime; got 'error'"):
            _ = parse_datetime("error")


class TestParseMonth:
    @given(month=months())
    def test_str(self, *, month: Month) -> None:
        result = parse_month(str(month))
        assert result == month

    @given(month=months())
    def test_isoformat(self, *, month: Month) -> None:
        result = parse_month(month.isoformat())
        assert result == month

    @given(month=months(), fmt=sampled_from(["%Y%m", "%Y %m"]).map(maybe_sub_pct_y))
    def test_various_formats(self, *, month: Month, fmt: str) -> None:
        result = parse_month(month.strftime(fmt))
        assert result == month

    def test_error(self) -> None:
        with raises(ParseMonthError, match="Unable to parse month; got 'error'"):
            _ = parse_month("error")


class TestParseTime:
    @given(time=times())
    def test_str(self, *, time: dt.time) -> None:
        result = parse_time(str(time))
        assert result == time

    @given(time=times())
    def test_isoformat(self, *, time: dt.time) -> None:
        result = parse_time(time.isoformat())
        assert result == time

    @given(time=times(), fmt=sampled_from(["%H%M%S.%f", "%H:%M:%S.%f"]))
    def test_hhmmss_fff(self, *, time: dt.time, fmt: str) -> None:
        result = parse_time(time.strftime(fmt))
        assert result == time

    @given(time=times(), fmt=sampled_from(["%H%M%S", "%H:%M:%S"]))
    def test_hhmmss(self, *, time: dt.time, fmt: str) -> None:
        time = time.replace(microsecond=0)
        result = parse_time(time.strftime(fmt))
        assert result == time

    @given(time=times(), fmt=sampled_from(["%H%M", "%H:%M"]))
    def test_hhmm(self, *, time: dt.time, fmt: str) -> None:
        time = time.replace(second=0, microsecond=0)
        result = parse_time(time.strftime(fmt))
        assert result == time

    @given(time=times())
    def test_hh(self, *, time: dt.time) -> None:
        time = time.replace(minute=0, second=0, microsecond=0)
        result = parse_time(time.strftime("%H"))
        assert result == time

    def test_error(self) -> None:
        with raises(ParseTimeError, match="Unable to parse time; got 'error'"):
            _ = parse_time("error")


class TestParseTimedelta:
    @given(timedelta=timedeltas())
    def test_main(self, *, timedelta: dt.timedelta) -> None:
        result = parse_timedelta(str(timedelta))
        assert result == timedelta

    def test_error(self) -> None:
        with raises(
            ParseTimedeltaError, match="Unable to parse timedelta; got 'error'"
        ):
            _ = parse_timedelta("error")


class TestSerialize:
    @given(data=data())
    @mark.parametrize(
        ("strategy", "serialize", "parse"),
        [
            param(dates(), serialize_date, parse_date),
            param(datetimes(timezones=just(UTC)), serialize_datetime, parse_datetime),
            param(months(), serialize_month, parse_month),
            param(times(), serialize_time, parse_time),
            param(timedeltas(), str, parse_timedelta),
            param(timedeltas(), serialize_timedelta, parse_timedelta),
        ],
    )
    def test_main(
        self,
        *,
        data: DataObject,
        strategy: SearchStrategy[Any],
        serialize: Callable[[Any], Any],
        parse: Callable[[Any], Any],
    ) -> None:
        value = data.draw(strategy)
        result = parse(serialize(value))
        assert result == value

    @given(datetime=datetimes())
    def test_serialize_date(self, *, datetime: dt.datetime) -> None:
        result = parse_date(serialize_date(datetime))
        assert result == datetime.date()


class TestRoundToWeekday:
    @given(date=dates())
    @settings(suppress_health_check={HealthCheck.filter_too_much})
    @mark.parametrize(
        ("func", "predicate", "operator"),
        [
            param(round_to_next_weekday, True, eq),
            param(round_to_next_weekday, False, gt),
            param(round_to_prev_weekday, True, eq),
            param(round_to_prev_weekday, False, lt),
        ],
    )
    def test_main(
        self,
        *,
        date: dt.date,
        func: Callable[[dt.date], dt.date],
        predicate: bool,
        operator: Callable[[dt.date, dt.date], bool],
    ) -> None:
        _ = assume(is_weekday(date) is predicate)
        with assume_does_not_raise(OverflowError):
            result = func(date)
        assert operator(result, date)


class TestTimedeltas:
    @mark.parametrize(
        "timedelta",
        [param(SECOND), param(MINUTE), param(HOUR), param(DAY), param(WEEK)],
    )
    def test_main(self, *, timedelta: dt.timedelta) -> None:
        assert isinstance(timedelta, dt.timedelta)


class TestTimeZones:
    def test_main(self) -> None:
        assert isinstance(UTC, dt.tzinfo)


class TestYieldDays:
    @given(start=dates(), days=integers(0, 365))
    def test_start_and_end(self, *, start: dt.date, days: int) -> None:
        with assume_does_not_raise(OverflowError):
            end = start + dt.timedelta(days=days)
            dates = list(yield_days(start=start, end=end))
        assert all(start <= d <= end for d in dates)

    @given(start=dates(), days=integers(0, 10))
    def test_start_and_days(self, *, start: dt.date, days: int) -> None:
        dates = list(yield_days(start=start, days=days))
        assert len(dates) == days
        assert all(d >= start for d in dates)

    @given(end=dates(), days=integers(0, 10))
    def test_end_and_days(self, *, end: dt.date, days: int) -> None:
        dates = list(yield_days(end=end, days=days))
        assert len(dates) == days
        assert all(d <= end for d in dates)

    def test_error(self) -> None:
        with raises(
            YieldDaysError, match="Invalid arguments: start=None, end=None, days=None"
        ):
            _ = list(yield_days())


class TestYieldWeekdays:
    @given(start=dates(), days=integers(0, 365))
    def test_start_and_end(self, *, start: dt.date, days: int) -> None:
        with assume_does_not_raise(OverflowError):
            end = start + dt.timedelta(days=days)
        dates = list(yield_weekdays(start=start, end=end))
        assert all(start <= d <= end for d in dates)
        assert all(map(is_weekday, dates))
        if is_weekday(start):
            assert start in dates
        if is_weekday(end):
            assert end in dates

    @given(start=dates(), days=integers(0, 10))
    def test_start_and_days(self, *, start: dt.date, days: int) -> None:
        dates = list(yield_weekdays(start=start, days=days))
        assert len(dates) == days
        assert all(d >= start for d in dates)
        assert all(map(is_weekday, dates))

    @given(end=dates(), days=integers(0, 10))
    def test_end_and_days(self, *, end: dt.date, days: int) -> None:
        dates = list(yield_weekdays(end=end, days=days))
        assert len(dates) == days
        assert all(d <= end for d in dates)
        assert all(map(is_weekday, dates))

    def test_error(self) -> None:
        with raises(
            YieldWeekdaysError,
            match="Invalid arguments: start=None, end=None, days=None",
        ):
            _ = list(yield_weekdays())

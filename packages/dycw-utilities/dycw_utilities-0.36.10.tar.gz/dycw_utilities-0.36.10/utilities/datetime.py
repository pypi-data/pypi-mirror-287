from __future__ import annotations

import datetime as dt
from contextlib import suppress
from dataclasses import dataclass, replace
from re import sub
from typing import TYPE_CHECKING, Any, Never, Self, assert_never, cast

from typing_extensions import override

from utilities.platform import SYSTEM, System
from utilities.re import ExtractGroupsError, extract_groups
from utilities.zoneinfo import (
    HONG_KONG,
    TOKYO,
    UTC,
    ensure_time_zone,
    get_time_zone_name,
)

if TYPE_CHECKING:
    from collections.abc import Iterator
    from zoneinfo import ZoneInfo

    from utilities.types import Duration

_DAYS_PER_YEAR = 365.25
SECOND = dt.timedelta(seconds=1)
MINUTE = dt.timedelta(minutes=1)
HOUR = dt.timedelta(hours=1)
DAY = dt.timedelta(days=1)
WEEK = dt.timedelta(weeks=1)
EPOCH_UTC = dt.datetime.fromtimestamp(0, tz=UTC)


def add_weekdays(date: dt.date, /, *, n: int = 1) -> dt.date:
    """Add a number of a weekdays to a given date.

    If the initial date is a weekend, then moving to the adjacent weekday
    counts as 1 move.
    """
    if n == 0 and not is_weekday(date):
        raise AddWeekdaysError(date)
    if n >= 1:
        for _ in range(n):
            date = round_to_next_weekday(date + dt.timedelta(days=1))
    elif n <= -1:
        for _ in range(-n):
            date = round_to_prev_weekday(date - dt.timedelta(days=1))
    return date


class AddWeekdaysError(Exception): ...


def date_to_datetime(
    date: dt.date, /, *, time: dt.time | None = None, time_zone: ZoneInfo | str = UTC
) -> dt.datetime:
    """Expand a date into a datetime."""
    time_use = dt.time(0) if time is None else time
    time_zone_use = ensure_time_zone(time_zone)
    return dt.datetime.combine(date, time_use, tzinfo=time_zone_use)


def date_to_month(date: dt.date, /) -> Month:
    """Collapse a date into a month."""
    return Month(year=date.year, month=date.month)


def duration_to_float(duration: Duration, /) -> float:
    """Ensure the duration is a float."""
    if isinstance(duration, int):
        return float(duration)
    if isinstance(duration, float):
        return duration
    return duration.total_seconds()


def duration_to_timedelta(duration: Duration, /) -> dt.timedelta:
    """Ensure the duration is a timedelta."""
    if isinstance(duration, int | float):
        return dt.timedelta(seconds=duration)
    return duration


def ensure_date(date: dt.date | str, /) -> dt.date:
    """Ensure the object is a date."""
    return date if isinstance(date, dt.date) else parse_date(date)


def ensure_datetime(
    datetime: dt.datetime | str, /, *, time_zone: ZoneInfo | str = UTC
) -> dt.datetime:
    """Ensure the object is a datetime."""
    if isinstance(datetime, dt.datetime):
        return datetime
    return parse_datetime(datetime, time_zone=time_zone)


def ensure_month(month: Month | str, /) -> Month:
    """Ensure the object is a month."""
    return month if isinstance(month, Month) else parse_month(month)


def ensure_time(time: dt.time | str, /) -> dt.time:
    """Ensure the object is a time."""
    return time if isinstance(time, dt.time) else parse_time(time)


def ensure_timedelta(timedelta: dt.timedelta | str, /) -> dt.timedelta:
    """Ensure the object is a timedelta."""
    if isinstance(timedelta, dt.timedelta):
        return timedelta
    return parse_timedelta(timedelta)


def format_datetime_local_and_utc(datetime: dt.datetime, /) -> str:
    """Format a local datetime locally & in UTC."""
    if (tzinfo := datetime.tzinfo) is None:
        raise FormatDatetimeLocalAndUTCError(datetime=datetime)
    time_zone = ensure_time_zone(tzinfo)
    if time_zone is UTC:
        return datetime.strftime("%Y-%m-%d %H:%M:%S (%a, UTC)")
    as_utc = datetime.astimezone(UTC)
    local = get_time_zone_name(time_zone)
    if datetime.year != as_utc.year:
        return f"{datetime:%Y-%m-%d %H:%M:%S (%a}, {local}, {as_utc:%Y-%m-%d %H:%M:%S} UTC)"
    if (datetime.month != as_utc.month) or (datetime.day != as_utc.day):
        return (
            f"{datetime:%Y-%m-%d %H:%M:%S (%a}, {local}, {as_utc:%m-%d %H:%M:%S} UTC)"
        )
    return f"{datetime:%Y-%m-%d %H:%M:%S (%a}, {local}, {as_utc:%H:%M:%S} UTC)"


@dataclass(kw_only=True)
class FormatDatetimeLocalAndUTCError(Exception):
    datetime: dt.datetime

    @override
    def __str__(self) -> str:
        return f"Datetime must have a time zone; got {self.datetime}"


def get_months(*, n: int = 1) -> dt.timedelta:
    """Get a number of months as a timedelta."""
    days_per_month = _DAYS_PER_YEAR / 12
    return dt.timedelta(days=round(n * days_per_month))


MONTH = get_months(n=1)


def get_now(*, time_zone: ZoneInfo | str = UTC) -> dt.datetime:
    """Get the current, timezone-aware time."""
    if time_zone == "local":
        from tzlocal import get_localzone

        time_zone_use = get_localzone()
    else:
        time_zone_use = ensure_time_zone(time_zone)
    return dt.datetime.now(tz=time_zone_use)


NOW_UTC = get_now(time_zone=UTC)


def get_now_hk() -> dt.datetime:
    """Get the current time in Hong Kong."""
    return dt.datetime.now(tz=HONG_KONG)


NOW_HK = get_now_hk()


def get_now_tokyo() -> dt.datetime:
    """Get the current time in Tokyo."""
    return dt.datetime.now(tz=TOKYO)


NOW_TOKYO = get_now_tokyo()


def get_quarters(*, n: int = 1) -> dt.timedelta:
    """Get a number of quarters as a timedelta."""
    days_per_quarter = _DAYS_PER_YEAR / 4
    return dt.timedelta(days=round(n * days_per_quarter))


QUARTER = get_quarters(n=1)


def get_today(*, time_zone: ZoneInfo | str = UTC) -> dt.date:
    """Get the current, timezone-aware date."""
    return get_now(time_zone=time_zone).date()


TODAY_UTC = get_today(time_zone=UTC)


def get_today_hk() -> dt.date:
    """Get the current date in Hong Kong."""
    return get_now_hk().date()


TODAY_HK = get_today_hk()


def get_today_tokyo() -> dt.date:
    """Get the current date in Tokyo."""
    return get_now_tokyo().date()


TODAY_TOKYO = get_today_tokyo()


def get_years(*, n: int = 1) -> dt.timedelta:
    """Get a number of years as a timedelta."""
    return dt.timedelta(days=round(n * _DAYS_PER_YEAR))


YEAR = get_years(n=1)


def is_equal_mod_tz(x: dt.datetime, y: dt.datetime, /) -> bool:
    """Check if x == y, modulo timezone."""
    x_aware, y_aware = x.tzinfo is not None, y.tzinfo is not None
    match x_aware, y_aware:
        case (False, False) | (True, True):
            return x == y
        case True, False:
            return x.astimezone(UTC).replace(tzinfo=None) == y
        case False, True:
            return x == y.astimezone(UTC).replace(tzinfo=None)
        case _ as never:
            assert_never(cast(Never, never))


def is_weekday(date: dt.date, /) -> bool:
    """Check if a date is a weekday."""
    friday = 5
    return date.isoweekday() <= friday


def maybe_sub_pct_y(text: str, /) -> str:
    """Substitute the `%Y' token with '%4Y' if necessary."""
    match SYSTEM:
        case System.windows:  # pragma: os-ne-windows
            return text
        case System.mac:  # pragma: os-ne-macos
            return text
        case System.linux:  # pragma: os-ne-linux
            return sub("%Y", "%4Y", text)
        case _ as never:  # pyright: ignore[reportUnnecessaryComparison]
            assert_never(never)


@dataclass(order=True, frozen=True)
class Month:
    """Represents a month in time."""

    year: int
    month: int

    def __post_init__(self) -> None:
        try:
            _ = dt.date(self.year, self.month, 1)
        except ValueError:
            raise MonthError(year=self.year, month=self.month) from None

    @override
    def __repr__(self) -> str:
        return serialize_month(self)

    @override
    def __str__(self) -> str:
        return repr(self)

    def __add__(self, other: Any, /) -> Self:
        if not isinstance(other, int):  # pragma: no cover
            return NotImplemented
        years, month = divmod(self.month + other - 1, 12)
        month += 1
        year = self.year + years
        return replace(self, year=year, month=month)

    def __sub__(self, other: Any, /) -> Self:
        if not isinstance(other, int):  # pragma: no cover
            return NotImplemented
        return self + (-other)

    def isoformat(self) -> str:
        return serialize_month(self)

    def strftime(self, format_: str) -> str:
        return self.to_date().strftime(format_)

    def to_date(self, /, *, day: int = 1) -> dt.date:
        return dt.date(self.year, self.month, day)


@dataclass(kw_only=True)
class MonthError(Exception):
    year: int
    month: int

    @override
    def __str__(self) -> str:
        return f"Invalid year and month: {self.year}, {self.month}"


MIN_MONTH = Month(dt.date.min.year, dt.date.min.month)
MAX_MONTH = Month(dt.date.max.year, dt.date.max.month)


def parse_date(date: str, /, *, time_zone: ZoneInfo | str = UTC) -> dt.date:
    """Parse a string into a date."""
    with suppress(ValueError):
        return dt.date.fromisoformat(date)
    time_zone_use = ensure_time_zone(time_zone)
    for fmt in ["%Y%m%d", "%Y %m %d", "%d%b%Y", "%d %b %Y"]:
        try:
            return dt.datetime.strptime(date, fmt).replace(tzinfo=time_zone_use).date()
        except ValueError:
            pass
    raise ParseDateError(date=date)


@dataclass(kw_only=True, slots=True)
class ParseDateError(Exception):
    date: str

    @override
    def __str__(self) -> str:
        return f"Unable to parse date; got {self.date!r}"


def parse_datetime(datetime: str, /, *, time_zone: ZoneInfo | str = UTC) -> dt.datetime:
    """Parse a string into a datetime."""
    time_zone_use = ensure_time_zone(time_zone)
    with suppress(ValueError):
        return dt.datetime.fromisoformat(datetime).replace(tzinfo=time_zone_use)
    for fmt in [
        "%Y%m%d",
        "%Y%m%dT%H",
        "%Y%m%dT%H%M",
        "%Y%m%dT%H%M%S",
        "%Y%m%dT%H%M%S.%f",
    ]:
        try:
            return dt.datetime.strptime(datetime, fmt).replace(tzinfo=time_zone_use)
        except ValueError:
            pass
    for fmt in ["%Y-%m-%d %H:%M:%S.%f%z", "%Y%m%dT%H%M%S.%f%z"]:
        try:
            return dt.datetime.strptime(datetime, fmt)  # noqa: DTZ007
        except ValueError:
            pass
    raise ParseDateTimeError(datetime=datetime)


@dataclass(kw_only=True, slots=True)
class ParseDateTimeError(Exception):
    datetime: str

    @override
    def __str__(self) -> str:
        return f"Unable to parse datetime; got {self.datetime!r}"


def parse_month(month: str, /) -> Month:
    """Parse a string into a month."""
    for fmt in ["%Y-%m", "%Y%m", "%Y %m"]:
        try:
            date = dt.datetime.strptime(month, fmt).replace(tzinfo=UTC).date()
        except ValueError:
            pass
        else:
            return Month(date.year, date.month)
    raise ParseMonthError(month=month)


@dataclass(kw_only=True, slots=True)
class ParseMonthError(Exception):
    month: str

    @override
    def __str__(self) -> str:
        return f"Unable to parse month; got {self.month!r}"


def parse_time(time: str, /) -> dt.time:
    """Parse a string into a time."""
    with suppress(ValueError):
        return dt.time.fromisoformat(time)
    for fmt in ["%H", "%H%M", "%H%M%S", "%H%M%S.%f"]:
        try:
            return dt.datetime.strptime(time, fmt).replace(tzinfo=UTC).time()
        except ValueError:
            pass
    raise ParseTimeError(time=time)


@dataclass(kw_only=True, slots=True)
class ParseTimeError(Exception):
    time: str

    @override
    def __str__(self) -> str:
        return f"Unable to parse time; got {self.time!r}"


def parse_timedelta(timedelta: str, /) -> dt.timedelta:
    """Parse a string into a timedelta."""

    def try_parse(fmt: str, /) -> dt.datetime | None:
        try:
            return dt.datetime.strptime(timedelta, fmt).replace(tzinfo=UTC)
        except ValueError:
            return None

    try:
        as_dt = next(
            parsed
            for fmt in ("%H:%M:%S", "%H:%M:%S.%f")
            if (parsed := try_parse(fmt)) is not None
        )
    except StopIteration:
        pass
    else:
        return dt.timedelta(
            hours=as_dt.hour,
            minutes=as_dt.minute,
            seconds=as_dt.second,
            microseconds=as_dt.microsecond,
        )
    try:
        days, tail = extract_groups(r"([-\d]+)\s*(?:days?)?,?\s*([\d:\.]+)", timedelta)
    except ExtractGroupsError:
        raise ParseTimedeltaError(timedelta=timedelta) from None
    return dt.timedelta(days=int(days)) + parse_timedelta(tail)


@dataclass(kw_only=True, slots=True)
class ParseTimedeltaError(Exception):
    timedelta: str

    @override
    def __str__(self) -> str:
        return f"Unable to parse timedelta; got {self.timedelta!r}"


def round_to_next_weekday(date: dt.date, /) -> dt.date:
    """Round a date to the next weekday."""
    return _round_to_weekday(date, is_next=True)


def round_to_prev_weekday(date: dt.date, /) -> dt.date:
    """Round a date to the previous weekday."""
    return _round_to_weekday(date, is_next=False)


def _round_to_weekday(date: dt.date, /, *, is_next: bool) -> dt.date:
    """Round a date to the previous weekday."""
    n = 1 if is_next else -1
    while not is_weekday(date):
        date = add_weekdays(date, n=n)
    return date


def serialize_date(date: dt.date, /) -> str:
    """Serialize a date."""
    if isinstance(date, dt.datetime):
        return serialize_date(date.date())
    return date.isoformat()


def serialize_datetime(datetime: dt.datetime, /) -> str:
    """Serialize a datetime."""
    return datetime.isoformat()


def serialize_month(month: Month, /) -> str:
    """Serialize a month."""
    return f"{month.year:04}-{month.month:02}"


def serialize_time(time: dt.time, /) -> str:
    """Serialize a time."""
    return time.isoformat()


def serialize_timedelta(timedelta: dt.timedelta, /) -> str:
    """Serialize a timedelta."""
    if (days := timedelta.days) == 0:
        return str(timedelta)
    tail = serialize_timedelta(timedelta - dt.timedelta(days=days))
    return f"d{days},{tail}"


def yield_days(
    *, start: dt.date | None = None, end: dt.date | None = None, days: int | None = None
) -> Iterator[dt.date]:
    """Yield the days in a range."""
    if (start is not None) and (end is not None) and (days is None):
        date = start
        while date <= end:
            yield date
            date += dt.timedelta(days=1)
        return
    if (start is not None) and (end is None) and (days is not None):
        date = start
        for _ in range(days):
            yield date
            date += dt.timedelta(days=1)
        return
    if (start is None) and (end is not None) and (days is not None):
        date = end
        for _ in range(days):
            yield date
            date -= dt.timedelta(days=1)
        return
    raise YieldDaysError(start=start, end=end, days=days)


@dataclass(kw_only=True, slots=True)
class YieldDaysError(Exception):
    start: dt.date | None
    end: dt.date | None
    days: int | None

    @override
    def __str__(self) -> str:
        return (
            f"Invalid arguments: start={self.start}, end={self.end}, days={self.days}"
        )


def yield_weekdays(
    *, start: dt.date | None = None, end: dt.date | None = None, days: int | None = None
) -> Iterator[dt.date]:
    """Yield the weekdays in a range."""
    if (start is not None) and (end is not None) and (days is None):
        date = round_to_next_weekday(start)
        while date <= end:
            yield date
            date = round_to_next_weekday(date + dt.timedelta(days=1))
        return
    if (start is not None) and (end is None) and (days is not None):
        date = round_to_next_weekday(start)
        for _ in range(days):
            yield date
            date = round_to_next_weekday(date + dt.timedelta(days=1))
        return
    if (start is None) and (end is not None) and (days is not None):
        date = round_to_prev_weekday(end)
        for _ in range(days):
            yield date
            date = round_to_prev_weekday(date - dt.timedelta(days=1))
        return
    raise YieldWeekdaysError(start=start, end=end, days=days)


@dataclass(kw_only=True, slots=True)
class YieldWeekdaysError(Exception):
    start: dt.date | None
    end: dt.date | None
    days: int | None

    @override
    def __str__(self) -> str:
        return (
            f"Invalid arguments: start={self.start}, end={self.end}, days={self.days}"
        )


__all__ = [
    "DAY",
    "EPOCH_UTC",
    "HOUR",
    "MAX_MONTH",
    "MINUTE",
    "MIN_MONTH",
    "MONTH",
    "NOW_HK",
    "NOW_TOKYO",
    "NOW_UTC",
    "QUARTER",
    "SECOND",
    "TODAY_HK",
    "TODAY_TOKYO",
    "TODAY_UTC",
    "WEEK",
    "YEAR",
    "AddWeekdaysError",
    "FormatDatetimeLocalAndUTCError",
    "Month",
    "MonthError",
    "ParseDateError",
    "ParseDateTimeError",
    "ParseMonthError",
    "ParseTimeError",
    "ParseTimedeltaError",
    "YieldDaysError",
    "YieldWeekdaysError",
    "add_weekdays",
    "date_to_datetime",
    "date_to_month",
    "duration_to_float",
    "duration_to_timedelta",
    "ensure_date",
    "ensure_datetime",
    "ensure_month",
    "ensure_time",
    "ensure_timedelta",
    "format_datetime_local_and_utc",
    "get_months",
    "get_now",
    "get_now_hk",
    "get_now_tokyo",
    "get_quarters",
    "get_today",
    "get_today_hk",
    "get_today_tokyo",
    "get_years",
    "is_weekday",
    "maybe_sub_pct_y",
    "parse_date",
    "parse_datetime",
    "parse_month",
    "parse_time",
    "parse_timedelta",
    "round_to_next_weekday",
    "round_to_prev_weekday",
    "serialize_date",
    "serialize_datetime",
    "serialize_month",
    "serialize_time",
    "serialize_timedelta",
    "yield_days",
    "yield_weekdays",
]

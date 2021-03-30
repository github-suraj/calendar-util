from . import util, from_year, from_range
from datetime import MAXYEAR, MINYEAR, date
from calendar import monthrange, monthcalendar

__positions = ("first", "last")

__delta = lambda n: n%5 + n//5

def __validate_input(year, month, position):
    if not (MINYEAR <= year <= MAXYEAR):
        raise ValueError(f"year {year} is out of range, year should be between {MINYEAR} - {MAXYEAR}")
    if not (1 <= month <= 12):
        raise ValueError(f"month {month} is out of range, month should be between 1 - 12")
    if position not in __positions:
        raise ValueError(f"{position} not in {__positions}")

def __date_of_month(year, month, position, weekday=False):
    __validate_input(year, month, position)
    start, last_day = monthrange(year, month)
    if position == 'first':
        day = 1
        if weekday:
            delta = __delta(start)
            if start != delta:
                day += 7 - start
    else:
        day = max(monthcalendar(year, month)[-1:][0][:5]) if weekday else last_day
    return date(year, month, day)

def first_day_of_month(year, month):
    return __date_of_month(year, month, 'first')

def last_day_of_month(year, month):
    return __date_of_month(year, month, 'last')

def first_weekday_of_month(year, month):
    return __date_of_month(year, month, 'first', weekday=True)

def last_weekday_of_month(year, month):
    return __date_of_month(year, month, 'last', weekday=True)

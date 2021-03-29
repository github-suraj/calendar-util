import calendar
from datetime import MAXYEAR, MINYEAR, date, timedelta

__positions = ("first", "second", "third", "fourth", "last")
__weekdays = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')

def __validate_input(year, month, day, position):
    if not (MINYEAR <= year <= MAXYEAR):
        raise ValueError(f"year {year} is out of range, year should be between {MINYEAR} - {MAXYEAR}")
    if not (1 <= month <= 12):
        raise ValueError(f"month {month} is out of range, month should be between 1 - 12")
    if position not in __positions:
        raise ValueError(f"{position} not in {__positions}")
    if day not in __weekdays:
        raise ValueError(f"{day} not in {__weekdays}")

def _date_of_month(year, month, day, position):
    __validate_input(year, month, day, position)
    start, end = calendar.monthrange(year, month)
    if position == 'last':
        _date = date(year, month, end)
        delta = (_date.weekday() - eval(f"calendar.{day}")) % 7
        _date_day = _date - timedelta(days=delta)
    else:
        _date = date(year, month, 1)
        delta = (eval(f"calendar.{day}") - start) % 7 + (__positions.index(position) * 7)
        _date_day = _date + timedelta(days=delta)
    return _date_day

class first:    
    def first_monday_of_month(year, month):
        return _date_of_month(year, month, 'MONDAY', 'first')

    def first_tuesday_of_month(year, month):
        return _date_of_month(year, month, 'TUESDAY', 'first')

    def first_wednesday_of_month(year, month):
        return _date_of_month(year, month, 'WEDNESDAY', 'first')

    def first_thursday_of_month(year, month):
        return _date_of_month(year, month, 'THURSDAY', 'first')

    def first_friday_of_month(year, month):
        return _date_of_month(year, month, 'FRIDAY', 'first')

    def first_saturday_of_month(year, month):
        return _date_of_month(year, month, 'SATURDAY', 'first')

    def first_sunday_of_month(year, month):
        return _date_of_month(year, month, 'SUNDAY', 'first')

class second:
    def second_monday_of_month(year, month):
        return _date_of_month(year, month, 'MONDAY', 'second')

    def second_tuesday_of_month(year, month):
        return _date_of_month(year, month, 'TUESDAY', 'second')

    def second_wednesday_of_month(year, month):
        return _date_of_month(year, month, 'WEDNESDAY', 'second')

    def second_thursday_of_month(year, month):
        return _date_of_month(year, month, 'THURSDAY', 'second')

    def second_friday_of_month(year, month):
        return _date_of_month(year, month, 'FRIDAY', 'second')

    def second_saturday_of_month(year, month):
        return _date_of_month(year, month, 'SATURDAY', 'second')

    def second_sunday_of_month(year, month):
        return _date_of_month(year, month, 'SUNDAY', 'second')

class third:
    def third_monday_of_month(year, month):
        return _date_of_month(year, month, 'MONDAY', 'third')

    def third_tuesday_of_month(year, month):
        return _date_of_month(year, month, 'TUESDAY', 'third')

    def third_wednesday_of_month(year, month):
        return _date_of_month(year, month, 'WEDNESDAY', 'third')

    def third_thursday_of_month(year, month):
        return _date_of_month(year, month, 'THURSDAY', 'third')

    def third_friday_of_month(year, month):
        return _date_of_month(year, month, 'FRIDAY', 'third')

    def third_saturday_of_month(year, month):
        return _date_of_month(year, month, 'SATURDAY', 'third')

    def third_sunday_of_month(year, month):
        return _date_of_month(year, month, 'SUNDAY', 'third')

class fourth:
    def fourth_monday_of_month(year, month):
        return _date_of_month(year, month, 'MONDAY', 'fourth')

    def fourth_tuesday_of_month(year, month):
        return _date_of_month(year, month, 'TUESDAY', 'fourth')

    def fourth_wednesday_of_month(year, month):
        return _date_of_month(year, month, 'WEDNESDAY', 'fourth')

    def fourth_thursday_of_month(year, month):
        return _date_of_month(year, month, 'THURSDAY', 'fourth')

    def fourth_friday_of_month(year, month):
        return _date_of_month(year, month, 'FRIDAY', 'fourth')

    def fourth_saturday_of_month(year, month):
        return _date_of_month(year, month, 'SATURDAY', 'fourth')

    def fourth_sunday_of_month(year, month):
        return _date_of_month(year, month, 'SUNDAY', 'fourth')

class last:
    def last_monday_of_month(year, month):
        return _date_of_month(year, month, 'MONDAY', 'last')

    def last_tuesday_of_month(year, month):
        return _date_of_month(year, month, 'TUESDAY', 'last')

    def last_wednesday_of_month(year, month):
        return _date_of_month(year, month, 'WEDNESDAY', 'last')

    def last_thursday_of_month(year, month):
        return _date_of_month(year, month, 'THURSDAY', 'last')

    def last_friday_of_month(year, month):
        return _date_of_month(year, month, 'FRIDAY', 'last')

    def last_saturday_of_month(year, month):
        return _date_of_month(year, month, 'SATURDAY', 'last')

    def last_sunday_of_month(year, month):
        return _date_of_month(year, month, 'SUNDAY', 'last')

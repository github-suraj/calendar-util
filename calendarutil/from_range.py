from datetime import date
from . import util

def __validate_input(date1, date2):
    if not isinstance(date1, date):
        raise TypeError(f"{date1} should be a date object as {repr(date.today())}")
    if not isinstance(date2, date):
        raise TypeError(f"{date2} should be a date object as {repr(date.today())}")
    return (date1, date2) if date1 <= date2 else (date2, date1)

def _date_of_month(date1, date2, day, position):
    date1, date2 = __validate_input(date1, date2)
    start_month = date1.month
    start_year = date1.year
    end_month = date2.month
    end_year = date2.year
    dates = list()
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            if (year == start_year and month < start_month) or \
                (year == end_year and month > end_month):
                continue
            command = "util.{p}.{p}_{d}_of_month(year, month)".format(p=position, d=day.lower())
            dt = eval(command)
            dates.append(dt)
    return dates

class first:    
    def first_monday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'MONDAY', 'first')

    def first_tuesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'TUESDAY', 'first')

    def first_wednesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'WEDNESDAY', 'first')

    def first_thursday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'THURSDAY', 'first')

    def first_friday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'FRIDAY', 'first')

    def first_saturday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SATURDAY', 'first')

    def first_sunday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SUNDAY', 'first')

class second:
    def second_monday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'MONDAY', 'second')

    def second_tuesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'TUESDAY', 'second')

    def second_wednesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'WEDNESDAY', 'second')

    def second_thursday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'THURSDAY', 'second')

    def second_friday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'FRIDAY', 'second')

    def second_saturday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SATURDAY', 'second')

    def second_sunday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SUNDAY', 'second')

class third:
    def third_monday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'MONDAY', 'third')

    def third_tuesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'TUESDAY', 'third')

    def third_wednesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'WEDNESDAY', 'third')

    def third_thursday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'THURSDAY', 'third')

    def third_friday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'FRIDAY', 'third')

    def third_saturday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SATURDAY', 'third')

    def third_sunday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SUNDAY', 'third')

class fourth:
    def fourth_monday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'MONDAY', 'fourth')

    def fourth_tuesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'TUESDAY', 'fourth')

    def fourth_wednesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'WEDNESDAY', 'fourth')

    def fourth_thursday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'THURSDAY', 'fourth')

    def fourth_friday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'FRIDAY', 'fourth')

    def fourth_saturday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SATURDAY', 'fourth')

    def fourth_sunday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SUNDAY', 'fourth')

class last:
    def last_monday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'MONDAY', 'last')

    def last_tuesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'TUESDAY', 'last')

    def last_wednesday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'WEDNESDAY', 'last')

    def last_thursday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'THURSDAY', 'last')

    def last_friday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'FRIDAY', 'last')

    def last_saturday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SATURDAY', 'last')

    def last_sunday_of_month(date1, date2):
        return _date_of_month(date1, date2, 'SUNDAY', 'last')

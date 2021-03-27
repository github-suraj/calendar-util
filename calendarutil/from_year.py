from datetime import MAXYEAR, MINYEAR
from calendarutil import util

def __validate_input(year):
    if not (MINYEAR <= year <= MAXYEAR):
        raise ValueError(f"year {year} is out of range, year should be between {MINYEAR} - {MAXYEAR}")

def date_of_month(year, day, position):
    __validate_input(year)
    dates = list()
    for month in range(1, 13):
        command = "util.{p}.{p}_{d}_of_month(year, month)".format(p=position, d=day.lower())
        dt = eval(command)
        dates.append(dt)
    return dates

class first:    
    def first_monday_of_month(year):
        return date_of_month(year, 'MONDAY', 'first')

    def first_tuesday_of_month(year):
        return date_of_month(year, 'TUESDAY', 'first')

    def first_wednesday_of_month(year):
        return date_of_month(year, 'WEDNESDAY', 'first')

    def first_thursday_of_month(year):
        return date_of_month(year, 'THURSDAY', 'first')

    def first_friday_of_month(year):
        return date_of_month(year, 'FRIDAY', 'first')

    def first_saturday_of_month(year):
        return date_of_month(year, 'SATURDAY', 'first')

    def first_sunday_of_month(year):
        return date_of_month(year, 'SUNDAY', 'first')

class second:
    def second_monday_of_month(year):
        return date_of_month(year, 'MONDAY', 'second')

    def second_tuesday_of_month(year):
        return date_of_month(year, 'TUESDAY', 'second')

    def second_wednesday_of_month(year):
        return date_of_month(year, 'WEDNESDAY', 'second')

    def second_thursday_of_month(year):
        return date_of_month(year, 'THURSDAY', 'second')

    def second_friday_of_month(year):
        return date_of_month(year, 'FRIDAY', 'second')

    def second_saturday_of_month(year):
        return date_of_month(year, 'SATURDAY', 'second')

    def second_sunday_of_month(year):
        return date_of_month(year, 'SUNDAY', 'second')

class third:
    def third_monday_of_month(year):
        return date_of_month(year, 'MONDAY', 'third')

    def third_tuesday_of_month(year):
        return date_of_month(year, 'TUESDAY', 'third')

    def third_wednesday_of_month(year):
        return date_of_month(year, 'WEDNESDAY', 'third')

    def third_thursday_of_month(year):
        return date_of_month(year, 'THURSDAY', 'third')

    def third_friday_of_month(year):
        return date_of_month(year, 'FRIDAY', 'third')

    def third_saturday_of_month(year):
        return date_of_month(year, 'SATURDAY', 'third')

    def third_sunday_of_month(year):
        return date_of_month(year, 'SUNDAY', 'third')

class fourth:
    def fourth_monday_of_month(year):
        return date_of_month(year, 'MONDAY', 'fourth')

    def fourth_tuesday_of_month(year):
        return date_of_month(year, 'TUESDAY', 'fourth')

    def fourth_wednesday_of_month(year):
        return date_of_month(year, 'WEDNESDAY', 'fourth')

    def fourth_thursday_of_month(year):
        return date_of_month(year, 'THURSDAY', 'fourth')

    def fourth_friday_of_month(year):
        return date_of_month(year, 'FRIDAY', 'fourth')

    def fourth_saturday_of_month(year):
        return date_of_month(year, 'SATURDAY', 'fourth')

    def fourth_sunday_of_month(year):
        return date_of_month(year, 'SUNDAY', 'fourth')

class last:
    def last_monday_of_month(year):
        return date_of_month(year, 'MONDAY', 'last')

    def last_tuesday_of_month(year):
        return date_of_month(year, 'TUESDAY', 'last')

    def last_wednesday_of_month(year):
        return date_of_month(year, 'WEDNESDAY', 'last')

    def last_thursday_of_month(year):
        return date_of_month(year, 'THURSDAY', 'last')

    def last_friday_of_month(year):
        return date_of_month(year, 'FRIDAY', 'last')

    def last_saturday_of_month(year):
        return date_of_month(year, 'SATURDAY', 'last')

    def last_sunday_of_month(year):
        return date_of_month(year, 'SUNDAY', 'last')

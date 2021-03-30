from . import month, quarter

'''
1. Calculate last friday of the month
    INPUT:
        year as YYYY & month as m
    USAGE:
        from calendarutil.util import last
        dt = last.last_friday_of_month(year, m)
            Ex. dt = last.last_friday_of_month(2021, 3)
    OUTPUT:
        date object

2. Calculate second friday of the month for a year
    INPUT:
        year as YYYY
    USAGE:
        from calendarutil.from_year import second
        dts = second.second_friday_of_month(year)
            Ex. dts = second.second_friday_of_month(2021)
    OUTPUT:
        list of date objects

3. Calculate first friday of the month between two date range
    INPUT:
        date1 and date2 as date object
    USAGE:
        from datetime import date
        from calendarutil.from_range import first
        dts = first.first_friday_of_month(date1, date2)
        Ex. dts = first.first_friday_of_month(date(2021, 3, 1), date(2021, 6, 1))
    OUTPUT:
        list of date objects
'''
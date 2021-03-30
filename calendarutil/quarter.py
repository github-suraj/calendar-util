from . import month

def __validate_input(qtr):
    if not (1 <= qtr <= 4):
        raise ValueError(f"quarter {qtr} is out of range, quarter should be between 1 - 4")

def __date_of_quarter(year, qtr, position, weekday=False):
    __validate_input(qtr)
    _month = (qtr - 1) * 3 + 1 if position == 'first' else qtr * 3
    if weekday:
        command = "month.{p}_weekday_of_month(year, _month)".format(p=position)
    else:
        command = "month.{p}_day_of_month(year, _month)".format(p=position)
    return eval(command)

def first_day_of_quarter(year, qtr):
    return __date_of_quarter(year, qtr, 'first')

def first_weekday_of_quarter(year, qtr):
    return __date_of_quarter(year, qtr, 'first', weekday=True)

def last_day_of_quarter(year, qtr):
    return __date_of_quarter(year, qtr, 'last')

def last_weekday_of_quarter(year, qtr):
    return __date_of_quarter(year, qtr, 'last', weekday=True)

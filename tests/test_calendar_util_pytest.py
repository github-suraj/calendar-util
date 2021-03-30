import sys
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(file_dir, '..')
sys.path.append(base_dir)

from tests import *
from calendarutil import month, quarter
from calendarutil.month import util, from_year, from_range

## Test case for class:first
def test_first_monday_of_month():
    assert util.first_monday_of_month(2021, 1) == fmom, "Test Failed"

def test_first_tuesday_of_month():
    assert util.first_tuesday_of_month(2021, 1) == ftum, "Test Failed"

def test_first_wednesday_of_monthh():
    assert util.first_wednesday_of_month(2021, 1) == fwem, "Test Failed"

def test_first_thursday_of_month():
    assert util.first_thursday_of_month(2021, 1) == fthm, "Test Failed"

def test_first_friday_of_month():
    assert util.first_friday_of_month(2021, 1) == ffrm, "Test Failed"

def test_first_saturday_of_month():
    assert util.first_saturday_of_month(2021, 1) == fsam, "Test Failed"

def test_first_sunday_of_month():
        assert util.first_sunday_of_month(2021, 1) == fsum, "Test Failed"

## Test case for class:second
def test_second_monday_of_month():
    assert util.second_monday_of_month(2021, 1) == smom, "Test Failed"

def test_second_tuesday_of_month():
    assert util.second_tuesday_of_month(2021, 1) == stum, "Test Failed"

def test_second_wednesday_of_monthh():
    assert util.second_wednesday_of_month(2021, 1) == swem, "Test Failed"

def test_second_thursday_of_month():
    assert util.second_thursday_of_month(2021, 1) == sthm, "Test Failed"

def test_second_friday_of_month():
    assert util.second_friday_of_month(2021, 1) == sfrm, "Test Failed"

def test_second_saturday_of_month():
    assert util.second_saturday_of_month(2021, 1) == ssam, "Test Failed"

def test_second_sunday_of_month():
    assert util.second_sunday_of_month(2021, 1) == ssum, "Test Failed"

## Test case for class:third
def test_third_monday_of_month():
    assert util.third_monday_of_month(2021, 1) == tmom, "Test Failed"

def test_third_tuesday_of_month():
    assert util.third_tuesday_of_month(2021, 1) == ttum, "Test Failed"

def test_third_wednesday_of_monthh():
    assert util.third_wednesday_of_month(2021, 1) == twem, "Test Failed"

def test_third_thursday_of_month():
    assert util.third_thursday_of_month(2021, 1) == tthm, "Test Failed"

def test_third_friday_of_month():
    assert util.third_friday_of_month(2021, 1) == tfrm, "Test Failed"

def test_third_saturday_of_month():
    assert util.third_saturday_of_month(2021, 1) == tsam, "Test Failed"

def test_third_sunday_of_month():
    assert util.third_sunday_of_month(2021, 1) == tsum, "Test Failed"

## Test case for class:fourth
def test_fourth_monday_of_month():
    assert util.fourth_monday_of_month(2021, 1) == frmom, "Test Failed"

def test_fourth_tuesday_of_month():
    assert util.fourth_tuesday_of_month(2021, 1) == frtum, "Test Failed"

def test_fourth_wednesday_of_monthh():
    assert util.fourth_wednesday_of_month(2021, 1) == frwem, "Test Failed"

def test_fourth_thursday_of_month():
    assert util.fourth_thursday_of_month(2021, 1) == frthm, "Test Failed"

def test_fourth_friday_of_month():
    assert util.fourth_friday_of_month(2021, 1) == frfrm, "Test Failed"

def test_fourth_saturday_of_month():
    assert util.fourth_saturday_of_month(2021, 1) == frsam, "Test Failed"

def test_fourth_sunday_of_month():
    assert util.fourth_sunday_of_month(2021, 1) == frsum, "Test Failed"

## Test case for class:last
def test_last_monday_of_month():
    assert util.last_monday_of_month(2021, 1) == lmom, "Test Failed"

def test_last_tuesday_of_month():
    assert util.last_tuesday_of_month(2021, 1) == ltum, "Test Failed"

def test_last_wednesday_of_monthh():
    assert util.last_wednesday_of_month(2021, 1) == lwem, "Test Failed"

def test_last_thursday_of_month():
    assert util.last_thursday_of_month(2021, 1) == lthm, "Test Failed"

def test_last_friday_of_month():
    assert util.last_friday_of_month(2021, 1) == lfrm, "Test Failed"

def test_last_saturday_of_month():
    assert util.last_saturday_of_month(2021, 1) == lsam, "Test Failed"

def test_last_sunday_of_month():
    assert util.last_sunday_of_month(2021, 1) == lsum, "Test Failed"

## Test case for class:from_year
def test_fy_first_monday_of_month():
    dts = from_year.first_monday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 6), "Test Failed"

## Test case for class:from_year
def test_fy_second_tuesday_of_month():
    dts = from_year.second_tuesday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 14), "Test Failed"

## Test case for class:from_year
def test_fy_third_wednesday_of_month():
    dts = from_year.third_wednesday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 15), "Test Failed"

## Test case for class:from_year
def test_fy_fourth_thursday_of_month():
    dts = from_year.fourth_thursday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 23), "Test Failed"

## Test case for class:from_year
def test_fy_last_friday_of_month():
    dts = from_year.last_friday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 31), "Test Failed"

## Test case for class:from_range
def test_fr_first_monday_of_month():
    dts = from_range.first_monday_of_month(date(2021, 1, 1), date(2021, 6, 1))
    assert len(dts) == 6, "Test Failed"
    assert dts[-2] == date(2021, 5, 3), "Test Failed"

## Test case for class:from_range
def test_fr_second_tuesday_of_month():
    dts = from_range.second_tuesday_of_month(date(2021, 2, 1), date(2021, 11, 1))
    assert len(dts) == 10, "Test Failed"
    assert dts[-3] == date(2021, 9, 14), "Test Failed"

## Test case for class:from_range
def test_fr_third_wednesday_of_month():
    dts = from_range.third_wednesday_of_month(date(2021, 3, 1), date(2021, 5, 1))
    assert dts == [date(2021, 3, 17), date(2021, 4, 21), date(2021, 5, 19)], "Test Failed"

## Test case for class:from_range
def test_fr_fourth_thursday_of_month():
    dts = from_range.fourth_thursday_of_month(date(2021, 4, 1), date(2021, 9, 1))
    assert len(dts) == 6, "Test Failed"
    assert dts[2:4] == [date(2021, 6, 24), date(2021, 7, 22)], "Test Failed"

## Test case for class:from_range
def test_fr_last_friday_of_month():
    dts = from_range.last_friday_of_month(date(2021, 6, 1), date(2021, 6, 1))
    assert dts == [date(2021, 6, 25)], "Test Failed"

## First day of month
def test_first_day_of_month():
    for i in range(1, 13):
        dt = month.first_day_of_month(2021, i)
        assert dt == date(2021, i, 1)

## Last day of month
def test_last_day_of_month():
    for i in range(1, 13):
        dt = month.last_day_of_month(2021, i)
        assert dt == ldom[i-1]
    dt = month.last_day_of_month(2024, 2)
    assert dt == date(2024, 2, 29)

## First weekday of month
def test_first_weekday_of_month():
    for i in range(1, 13):
        dt = month.first_weekday_of_month(2021, i)
        assert dt == fwdom[i-1]

## Last weekday of month
def test_last_weekday_of_month():
    for i in range(1, 13):
        dt = month.last_weekday_of_month(2021, i)
        assert dt == lwdom[i-1]

## First day of quarter
def test_first_day_of_quarter():
    for i in range(1, 5):
        dt = quarter.first_day_of_quarter(2021, i)
        assert dt == fdoq[i-1]

## Last day of quarter
def test_last_day_of_quarter():
    for i in range(1, 5):
        dt = quarter.last_day_of_quarter(2021, i)
        assert dt == ldoq[i-1]

## First weekday of quarter
def test_first_weekday_of_quarter():
    for i in range(1, 5):
        dt = quarter.first_weekday_of_quarter(2021, i)
        assert dt == fdoq[i-1]

## Last weekday of quarter
def test_last_weekday_of_quarter():
    for i in range(1, 5):
        dt = quarter.last_weekday_of_quarter(2021, i)
        assert dt == ldoq[i-1]
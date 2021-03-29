import sys
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(file_dir, '..')
sys.path.append(base_dir)

from calendarutil import from_year, from_range
from datetime import date

## Test case for class:from_year.first
def test_fy_first_monday_of_month():
    dts = from_year.first.first_monday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 6), "Test Failed"

## Test case for class:from_year.second
def test_fy_second_tuesday_of_month():
    dts = from_year.second.second_tuesday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 14), "Test Failed"

## Test case for class:from_year.third
def test_fy_third_wednesday_of_month():
    dts = from_year.third.third_wednesday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 15), "Test Failed"

## Test case for class:from_year.fourth
def test_fy_fourth_thursday_of_month():
    dts = from_year.fourth.fourth_thursday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 23), "Test Failed"

## Test case for class:from_year.last
def test_fy_last_friday_of_month():
    dts = from_year.last.last_friday_of_month(2021)
    assert len(dts) == 12, "Test Failed"
    assert dts[-1] == date(2021, 12, 31), "Test Failed"

## Test case for class:from_range.first
def test_fr_first_monday_of_month():
    dts = from_range.first.first_monday_of_month(date(2021, 1, 1), date(2021, 6, 1))
    assert len(dts) == 6, "Test Failed"
    assert dts[-2] == date(2021, 5, 3), "Test Failed"

## Test case for class:from_range.second
def test_fr_second_tuesday_of_month():
    dts = from_range.second.second_tuesday_of_month(date(2021, 2, 1), date(2021, 11, 1))
    assert len(dts) == 10, "Test Failed"
    assert dts[-3] == date(2021, 9, 14), "Test Failed"

## Test case for class:from_range.third
def test_fr_third_wednesday_of_month():
    dts = from_range.third.third_wednesday_of_month(date(2021, 3, 1), date(2021, 5, 1))
    assert dts == [date(2021, 3, 17), date(2021, 4, 21), date(2021, 5, 19)], "Test Failed"
## Test case for class:from_range.fourth
def test_fr_fourth_thursday_of_month():
    dts = from_range.fourth.fourth_thursday_of_month(date(2021, 4, 1), date(2021, 9, 1))
    assert len(dts) == 6, "Test Failed"
    assert dts[2:4] == [date(2021, 6, 24), date(2021, 7, 22)], "Test Failed"

## Test case for class:from_range.last
def test_fr_last_friday_of_month():
    dts = from_range.last.last_friday_of_month(date(2021, 6, 1), date(2021, 6, 1))
    assert dts == [date(2021, 6, 25)], "Test Failed"
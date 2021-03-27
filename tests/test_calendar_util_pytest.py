import sys
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(file_dir, '..')
sys.path.append(base_dir)

from tests import *
from calendarutil.util import *

## Test case for class:first
def test_first_monday_of_month():
    assert first.first_monday_of_month(2021, 1) == fmom, "Test Failed"

def test_first_tuesday_of_month():
    assert first.first_tuesday_of_month(2021, 1) == ftum, "Test Failed"

def test_first_wednesday_of_monthh():
    assert first.first_wednesday_of_month(2021, 1) == fwem, "Test Failed"

def test_first_thursday_of_month():
    assert first.first_thursday_of_month(2021, 1) == fthm, "Test Failed"

def test_first_friday_of_month():
    assert first.first_friday_of_month(2021, 1) == ffrm, "Test Failed"

def test_first_saturday_of_month():
    assert first.first_saturday_of_month(2021, 1) == fsam, "Test Failed"

def test_first_sunday_of_month():
        assert first.first_sunday_of_month(2021, 1) == fsum, "Test Failed"

## Test case for class:second
def test_second_monday_of_month():
    assert second.second_monday_of_month(2021, 1) == smom, "Test Failed"

def test_second_tuesday_of_month():
    assert second.second_tuesday_of_month(2021, 1) == stum, "Test Failed"

def test_second_wednesday_of_monthh():
    assert second.second_wednesday_of_month(2021, 1) == swem, "Test Failed"

def test_second_thursday_of_month():
    assert second.second_thursday_of_month(2021, 1) == sthm, "Test Failed"

def test_second_friday_of_month():
    assert second.second_friday_of_month(2021, 1) == sfrm, "Test Failed"

def test_second_saturday_of_month():
    assert second.second_saturday_of_month(2021, 1) == ssam, "Test Failed"

def test_second_sunday_of_month():
    assert second.second_sunday_of_month(2021, 1) == ssum, "Test Failed"

## Test case for class:third
def test_third_monday_of_month():
    assert third.third_monday_of_month(2021, 1) == tmom, "Test Failed"

def test_third_tuesday_of_month():
    assert third.third_tuesday_of_month(2021, 1) == ttum, "Test Failed"

def test_third_wednesday_of_monthh():
    assert third.third_wednesday_of_month(2021, 1) == twem, "Test Failed"

def test_third_thursday_of_month():
    assert third.third_thursday_of_month(2021, 1) == tthm, "Test Failed"

def test_third_friday_of_month():
    assert third.third_friday_of_month(2021, 1) == tfrm, "Test Failed"

def test_third_saturday_of_month():
    assert third.third_saturday_of_month(2021, 1) == tsam, "Test Failed"

def test_third_sunday_of_month():
    assert third.third_sunday_of_month(2021, 1) == tsum, "Test Failed"

## Test case for class:fourth
def test_fourth_monday_of_month():
    assert fourth.fourth_monday_of_month(2021, 1) == frmom, "Test Failed"

def test_fourth_tuesday_of_month():
    assert fourth.fourth_tuesday_of_month(2021, 1) == frtum, "Test Failed"

def test_fourth_wednesday_of_monthh():
    assert fourth.fourth_wednesday_of_month(2021, 1) == frwem, "Test Failed"

def test_fourth_thursday_of_month():
    assert fourth.fourth_thursday_of_month(2021, 1) == frthm, "Test Failed"

def test_fourth_friday_of_month():
    assert fourth.fourth_friday_of_month(2021, 1) == frfrm, "Test Failed"

def test_fourth_saturday_of_month():
    assert fourth.fourth_saturday_of_month(2021, 1) == frsam, "Test Failed"

def test_fourth_sunday_of_month():
    assert fourth.fourth_sunday_of_month(2021, 1) == frsum, "Test Failed"

## Test case for class:last
def test_last_monday_of_month():
    assert last.last_monday_of_month(2021, 1) == lmom, "Test Failed"

def test_last_tuesday_of_month():
    assert last.last_tuesday_of_month(2021, 1) == ltum, "Test Failed"

def test_last_wednesday_of_monthh():
    assert last.last_wednesday_of_month(2021, 1) == lwem, "Test Failed"

def test_last_thursday_of_month():
    assert last.last_thursday_of_month(2021, 1) == lthm, "Test Failed"

def test_last_friday_of_month():
    assert last.last_friday_of_month(2021, 1) == lfrm, "Test Failed"

def test_last_saturday_of_month():
    assert last.last_saturday_of_month(2021, 1) == lsam, "Test Failed"

def test_last_sunday_of_month():
    assert last.last_sunday_of_month(2021, 1) == lsum, "Test Failed"

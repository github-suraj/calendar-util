import sys
import os
import unittest

file_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(file_dir, '..')
sys.path.append(base_dir)

from tests import *
from calendarutil.month import util

class UtilFirst(unittest.TestCase):
    def test_first_monday_of_month(self):
        self.assertEqual(util.first_monday_of_month(2021, 1), fmom)

    def test_first_tuesday_of_month(self):
        self.assertEqual(util.first_tuesday_of_month(2021, 1), ftum)

    def test_first_wednesday_of_monthh(self):
        self.assertEqual(util.first_wednesday_of_month(2021, 1), fwem)

    def test_first_thursday_of_month(self):
        self.assertEqual(util.first_thursday_of_month(2021, 1), fthm)

    def test_first_friday_of_month(self):
        self.assertEqual(util.first_friday_of_month(2021, 1), ffrm)

    def test_first_saturday_of_month(self):
        self.assertEqual(util.first_saturday_of_month(2021, 1), fsam)

    def test_first_sunday_of_month(self):
        self.assertEqual(util.first_sunday_of_month(2021, 1), fsum)

class UtilSecond(unittest.TestCase):
    def test_second_monday_of_month(self):
        self.assertEqual(util.second_monday_of_month(2021, 1), smom)

    def test_second_tuesday_of_month(self):
        self.assertEqual(util.second_tuesday_of_month(2021, 1), stum)

    def test_second_wednesday_of_monthh(self):
        self.assertEqual(util.second_wednesday_of_month(2021, 1), swem)

    def test_second_thursday_of_month(self):
        self.assertEqual(util.second_thursday_of_month(2021, 1), sthm)

    def test_second_friday_of_month(self):
        self.assertEqual(util.second_friday_of_month(2021, 1), sfrm)

    def test_second_saturday_of_month(self):
        self.assertEqual(util.second_saturday_of_month(2021, 1), ssam)

    def test_second_sunday_of_month(self):
        self.assertEqual(util.second_sunday_of_month(2021, 1), ssum)

class UtilThird(unittest.TestCase):
    def test_third_monday_of_month(self):
        self.assertEqual(util.third_monday_of_month(2021, 1), tmom)

    def test_third_tuesday_of_month(self):
        self.assertEqual(util.third_tuesday_of_month(2021, 1), ttum)

    def test_third_wednesday_of_monthh(self):
        self.assertEqual(util.third_wednesday_of_month(2021, 1), twem)

    def test_third_thursday_of_month(self):
        self.assertEqual(util.third_thursday_of_month(2021, 1), tthm)

    def test_third_friday_of_month(self):
        self.assertEqual(util.third_friday_of_month(2021, 1), tfrm)

    def test_third_saturday_of_month(self):
        self.assertEqual(util.third_saturday_of_month(2021, 1), tsam)

    def test_third_sunday_of_month(self):
        self.assertEqual(util.third_sunday_of_month(2021, 1), tsum)

class UtilFourth(unittest.TestCase):
    def test_fourth_monday_of_month(self):
        self.assertEqual(util.fourth_monday_of_month(2021, 1), frmom)

    def test_fourth_tuesday_of_month(self):
        self.assertEqual(util.fourth_tuesday_of_month(2021, 1), frtum)

    def test_fourth_wednesday_of_monthh(self):
        self.assertEqual(util.fourth_wednesday_of_month(2021, 1), frwem)

    def test_fourth_thursday_of_month(self):
        self.assertEqual(util.fourth_thursday_of_month(2021, 1), frthm)

    def test_fourth_friday_of_month(self):
        self.assertEqual(util.fourth_friday_of_month(2021, 1), frfrm)

    def test_fourth_saturday_of_month(self):
        self.assertEqual(util.fourth_saturday_of_month(2021, 1), frsam)

    def test_fourth_sunday_of_month(self):
        self.assertEqual(util.fourth_sunday_of_month(2021, 1), frsum)

class UtilLast(unittest.TestCase):
    def test_last_monday_of_month(self):
        self.assertEqual(util.last_monday_of_month(2021, 1), lmom)

    def test_last_tuesday_of_month(self):
        self.assertEqual(util.last_tuesday_of_month(2021, 1), ltum)

    def test_last_wednesday_of_monthh(self):
        self.assertEqual(util.last_wednesday_of_month(2021, 1), lwem)

    def test_last_thursday_of_month(self):
        self.assertEqual(util.last_thursday_of_month(2021, 1), lthm)

    def test_last_friday_of_month(self):
        self.assertEqual(util.last_friday_of_month(2021, 1), lfrm)

    def test_last_saturday_of_month(self):
        self.assertEqual(util.last_saturday_of_month(2021, 1), lsam)

    def test_last_sunday_of_month(self):
        self.assertEqual(util.last_sunday_of_month(2021, 1), lsum)

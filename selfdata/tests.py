# from django.test import TestCase

# Create your tests here.

import unittest
from .utils import month_to_week


class Test_MonthToWeek_Monthod(unittest.TestCase):

    def test_values(self):
        self.assertEqual(month_to_week('2017-08', '2017-09'), ('2017-W31', '2017-W39'))
        self.assertEqual(month_to_week('2016-01', '2016-03'), ('2015-W53', '2016-W13'))
        self.assertEqual(month_to_week('2017-04', '2017-08'), ('2017-W13', '2017-W35'))


if __name__ == '__main__':
    unittest.main()
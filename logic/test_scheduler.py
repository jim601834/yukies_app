import unittest
from scheduler import get_date

class TestGetDate(unittest.TestCase):

    def test_first_monday(self):
        self.assertEqual(get_date('first Monday', 2024, 1), '2024-01-01')

    def test_second_tuesday(self):
        self.assertEqual(get_date('2nd Tue', 2024, 1), '2024-01-09')

    def test_third_wednesday(self):
        self.assertEqual(get_date('3rd Wed', 2024, 1), '2024-01-17')

    def test_fourth_thursday(self):
        self.assertEqual(get_date('4th Thu', 2024, 1), '2024-01-25')

    def test_last_friday(self):
        self.assertEqual(get_date('last Fri', 2024, 1), '2024-01-26')

    def test_specific_day(self):
        self.assertEqual(get_date('15', 2024, 1), '2024-01-15')

    def test_first_day(self):
        self.assertEqual(get_date('First Day', 2024, 1), '2024-01-01')

    def test_1st_day(self):
        self.assertEqual(get_date('1st Day', 2024, 1), '2024-01-01')

    def test_last_day(self):
        self.assertEqual(get_date('Last Day', 2024, 1), '2024-01-31')

    def test_10th_day(self):
        self.assertEqual(get_date('10th Day', 2024, 1), '2024-01-10')

    def test_tenth_day(self):
        self.assertEqual(get_date('Tenth Day', 2024, 1), '2024-01-10')

    def test_20th_day(self):
        self.assertEqual(get_date('20th Day', 2024, 1), '2024-01-20')

    def test_twentieth_day(self):
        self.assertEqual(get_date('Twentieth Day', 2024, 1), '2024-01-20')

    def test_invalid_day_of_week(self):
        self.assertEqual(get_date('first Funday', 2024, 1), 'Invalid day of the week')

    def test_invalid_ordinal(self):
        self.assertEqual(get_date('fifth Monday', 2024, 1), 'Invalid ordinal')

    def test_invalid_day_of_month(self):
        self.assertEqual(get_date('32', 2024, 1), 'Invalid day of the month')

if __name__ == '__main__':
    unittest.main()
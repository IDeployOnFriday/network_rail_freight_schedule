import unittest

from dates import is_date_between


class test_dates(unittest.TestCase):

    def test_simple_dates(self):
        start_date = '2024-01-1'
        end_date = '2024-01-20'
        self.assertTrue(is_date_between(start_date, end_date, '2024-01-10'))
        self.assertFalse(is_date_between(start_date, end_date, '2024-01-22'))

    def test_more_dates(self):
        start_date = '2023-12-22'
        end_date = '2024-01-01'
        self.assertTrue(is_date_between(start_date, end_date, '2023-12-28'))
        self.assertFalse(is_date_between(start_date, end_date, '2024-01-02'))

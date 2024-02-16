import unittest
from datetime import datetime, timedelta
from app.use_case.date_checker import DateChecker

class DateCheckerTest(unittest.TestCase):
    def test_get_first_date_of_week_from_a_date(self):
        date_checker = DateChecker()
        first_of_week = date_checker.get_first_of_week_from_date('2019-07-31')
        self.assertEqual((datetime.strptime('2019-07-31', '%Y-%m-%d') - timedelta(days=2)).strftime('%Y-%m-%d'), first_of_week)

    def test_get_dates_in_week_of_date(self):
        date_checker = DateChecker()
        dates_in_week_of_given_date = date_checker.get_dates_in_week_of_date('2019-07-31')
        self.assertEqual(7, len(dates_in_week_of_given_date))
        self.assertEqual((datetime.strptime('2019-07-31', '%Y-%m-%d') + timedelta(days=4)).strftime('%Y-%m-%d'), dates_in_week_of_given_date[6])

if __name__ == '__main__':
    unittest.main()
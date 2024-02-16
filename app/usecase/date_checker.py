from datetime import datetime, timedelta

class DateChecker:
    def get_first_of_week_from_date(self, date):
        day_of_week = date.weekday()
        first_of_week = date - timedelta(days=day_of_week)
        return first_of_week

    def get_dates_in_week_of_date(self, date):
        first_day_of_week = self.get_first_of_week_from_date(date)
        dates_in_week_of_date = [first_day_of_week + timedelta(days=i) for i in range(7)]
        return dates_in_week_of_date
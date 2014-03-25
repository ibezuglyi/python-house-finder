__author__ = 'dit'

from datetime import datetime, date


class TimeConverter():
    def __init__(self):
        self.months = ['sty', 'lut', 'mar']

    def get_date(self, datestr):
        now = datetime.now()
        if datestr.find("dzisiaj") >= 0:
            month = now.month
            day = now.day
        elif datestr.find("wczoraj")>=0:
            month = now.month
            day = now.day-1
        else:
            date_parts = datestr.split()
            day = int(date_parts[0])
            month = self.months.index(date_parts[1]) + 1

        return date(now.year, month, day)

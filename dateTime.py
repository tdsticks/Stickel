# -*- coding: utf-8 -*-
import datetime
import time

__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"


class DateTime:

    def __init__(self, debug=None):
        if debug: print "::Datetime::__init__"

        self.debug = debug

        # self.get_datetime()

    def months(self):
        if self.debug: print "::Datetime::months"

        months = {
            "01": "JAN",
            "02": "FEB",
            "03": "MAR",
            "04": "APR",
            "05": "MAY",
            "06": "JUN",
            "07": "JUL",
            "08": "AUG",
            "09": "SEP",
            "10": "OCT",
            "11": "NOV",
            "12": "DEC"
        }

        return months

    def get_now(self):
        if self.debug: print "::Datetime::get_now"

        now = datetime.datetime.today()
        # print "now:", now

        return now

    def get_todays_date(self):
        if self.debug: print "::Datetime::get_todays_date"

        now = self.get_now()
        add_zero = self.add_zero
        todays_date = add_zero(now.year) + add_zero(now.month) + add_zero(now.day)
        # print "todays_date:", todays_date

        return todays_date

    def get_datetime(self):
        if self.debug: print "::Datetime::get_datetime"

        now = self.get_now()
        todays_date = self.get_todays_date()
        add_zero = self.add_zero

        todays_datetime = todays_date + add_zero(now.hour) + add_zero(now.minute) + add_zero(now.second)
        #print "todays_datetime:", todays_datetime

        return todays_datetime

    def get_fmt_datetime(self):
        if self.debug: print "::Datetime::get_fmt_datetime"

        now = self.get_now()
        add_zero = self.add_zero

        todays_fmt_datetime = add_zero(now.year) + "/" + add_zero(now.month) + "/" + \
                              add_zero(now.day) + " " + add_zero(now.hour) + ":" + \
                              add_zero(now.minute) + ":" + add_zero(now.second) + " " + \
                              self.am_pm(now.hour)

        return todays_fmt_datetime

    def get_dt_with_epoch(self, epoch_sec):
        if self.debug: print "::Datetime::get_dt_with_epoch"

        local_time = time.localtime(epoch_sec)
        formatted_time = time.strftime("%a, %d %b %Y %H:%M:%S %p", local_time)

        return formatted_time

    def get_year(self):
        if self.debug: print "::Datetime::get_year"

        todaysDate = datetime.date.today()
        splitTodaysDate = str(todaysDate).split("-")
        year = splitTodaysDate[0]
        month = splitTodaysDate[1]
        date = splitTodaysDate[2]
        # print year, month, date

        return year

    def get_month_name(self):
        if self.debug: print "::Datetime::get_year"

        todaysDate = datetime.date.today()
        monthName = todaysDate.strftime('%b')

        return monthName

    @staticmethod
    def am_pm(hour):
        am_pm = "am"
        if hour > 12:
            am_pm = "pm"

        return am_pm

    @staticmethod
    def add_zero(num):

        if num < 10:
            num = "0" + str(num)
            return num
        else:
            return str(num)

if __name__ == "__main__":

    # Get date and time
    dt = DateTime(debug=True)
    print dt.get_fmt_datetime()
    #print dt.get_dt_with_epoch(1454607216)
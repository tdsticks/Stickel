# -*- coding: utf-8 -*-
try:
    from logger import Logger
except ImportError as err:
    print "ERROR >>> Could not import 'logger' <<<", err
    from logger import Logger

__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"


class PercentageClass:

    def __init__(self, name):
        #print "percentage::__init__"

        logger = Logger(name)
        self.log = logger.log

        # self.log( 1, "percentage::__init__" )

        self.count = 0

    def output_percentage(self, title, total, cur):
        percentage = round((100 * cur) / total)

        # self.log( 1, title +  " percent complete: " + str(percentage) + "%" )

        if percentage >= 10 * self.count:
            percentage_log = title + " percent complete: " + str(percentage) + "%"
            self.log(1, percentage_log)
            self.count = self.count + 1

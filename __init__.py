# -*- coding: utf-8 -*-
import os
import sys

try:
    import logger
except ImportError as err:
    print "ERROR >>> Could not import 'logger' <<<", err
    import logger

try:
    import dateTime
except ImportError as err:
    print "ERROR >>> Could not import 'dateTime' <<<", err
    import dateTime

# try:
#     import db
# except ImportError as err:
#     print "ERROR >>> Could not import 'db' <<<", err
#     import db

try:
    import fileUtility
except ImportError as err:
    print "ERROR >>> Could not import 'fileUtility' <<<", err
    import fileUtility


__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"


class Globals:

    def __init__(self, debug=None):
        if debug: print "::Globals::__init__"

        #
        # Init the globals
        #
        self.platform = sys.platform
        self.system = ""
        self.system_name = ""
        self.username = ""
        self.ds = ""  # Directory Separator

        self.ntwk_path = ""
        self.logs_path = ""

        self.debug = debug  # Just for debugging paths

        #
        # Run the methods (set the globals)
        #
        self.detect_os()
        self.set_paths()

    def detect_os(self):
        if self.debug: print "::Globals::detect_os"

        if self.platform.startswith('darwin'):
            import pwd
            self.system = "Osx"
            self.system_name = os.uname()[1]
            self.ds = "/"
            self.ntwk_path = os.getcwd() + self.ds
            self.username = pwd.getpwuid(os.getuid())[0]

        elif self.platform.startswith('linux'):
            self.system = "Linux"
            self.system_name = os.uname()[1]
            self.ds = "/"
            self.ntwk_path = os.getcwd() + self.ds

        self.ntwk_path = self.cnvrt_slsh(self.ntwk_path)

        if not os.path.exists(self.ntwk_path):
            print "Error: network path", self.ntwk_path, "does not exist!!!"
            print " platform:", self.platform
            print " system:", self.system
            print " system_name:", self.system_name
            print " username:", self.username
            print " dir_sep:", self.ds

        #
        # Whether or not these print out (for debugging)
        if self.debug:
            print " platform:", self.platform
            print " system:", self.system
            print " system_name:", self.system_name
            print " username:", self.username
            print " dir_sep:", self.ds
            print

    def set_paths(self):
        if self.debug: print "::Globals::set_paths"

        self.logs_path = self.ntwk_path + "logs" + self.ds

        #
        # Check the paths
        #
        if not os.path.exists(self.logs_path):
            print "Error: Logs path:", self.logs_path, "does not exist!!!"

        # print sys.path

        #
        # Whether or not these print out (for debugging)
        if self.debug:
            print "Paths:"
            print " ntwk:", self.ntwk_path
            print " logs:", self.logs_path
            print

    @staticmethod
    def cnvrt_slsh(path):
        # Convert backslashes to forward
        path = path.replace("\\", "//")
        return path


if __name__ == '__main__':

    print ">>> Running `__init__.Globals` module stand alone! <<<"

    Globals(debug=True)

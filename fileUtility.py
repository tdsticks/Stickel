# -*- coding: utf-8 -*-
import os
import re
import sys
import pysftp
import shutil

# https://docs.python.org/2.7/library/csv.html#csv.Sniffer
# import csv

try:
    import __init__
except ImportError as err:
    print "ERROR >>> Could not import __init__ <<<", err
    import __init__

__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"


class FileUtility:

    def __init__(self, debug=None):
        if debug: print "::FileUtility::__init__"

        self.debug = debug

        # Get global vars
        self.g = __init__.Globals()

    def read_dir(self, dir_path):
        if self.debug: print "::FileUtility::read_dir"

        file_list = []

        # If we can get access to the system, see if the file exists
        if os.path.exists(dir_path):

            for dir, subdir, files in os.walk(dir_path):
                # print dir

                for f in files:
                    # print f
                    file_path = dir + self.g.ds + f
                    # if self.debug: print file_path

                    file_list.append(file_path)

        return file_list

    def read_file(self, file_path):
        if self.debug: print "::FileUtility::read_file"

        file_data = []

        # If we can get access to the system, see if the file exists
        if os.path.exists(file_path):
            print "file_path", file_path

            with open(file_path) as fp:
                for line in fp:
                    # if self.debug: print line
                    file_data.append(line.strip("\n").strip("\r").rstrip())

        return file_data

    def read_raw_file(self, file_path):
        if self.debug: print "::FileUtility::read_raw_file"

        file_data = ""

        # If we can get access to the system, see if the file exists
        if os.path.exists(file_path):
            print "file_path", file_path

            with open(file_path) as fp:
                file_data = fp.read()

        return file_data

    def find_delimiter(self, string):
        if self.debug: print "::FileUtility::find_delimiter"
        # print string

        split_count = 0

        patterns = {
            "pipe": "|",
            # "carets": "^",
            "tildes": "~",
            "comma": ",",
            "semicolon": ";",
            "space": " ",
            "tab": "   "
        }

        selected_delimiter = patterns['semicolon']

        #
        # Search and find the delimiter
        #
        for p in patterns:
            # print p, patterns[p]
            match = re.search(patterns[p], string.rstrip())

            if match is not None:
                # print "found:", p
                # print " match:", match

                cur_split_count = len(string.split(patterns[p]))

                if cur_split_count > split_count:
                    # print " cur_split_count", cur_split_count
                    selected_delimiter = patterns[p]

                split_count = cur_split_count
            else:
                # print "not found:", p
                pass

        # print "selected_delimiter", selected_delimiter
        return selected_delimiter

    def standardize_field_headers(self, fields):
        if self.debug: print "::ET::standardize_field_headers"

        std_fields = map(lambda x: x.lower().replace(" ", "_"), fields)

        return std_fields

    def write_file(self, file_path, data):
        if self.debug: print "::FileUtility::write_file"

        target = open(file_path, 'a')

        target.write(data)

        target.close()


    def copy_file(self, file_name, source_path, destination_path):
        if self.debug: print "::FileUtility::copy_file"

        src_full_path = source_path + file_name
        # print "src_full_path:", src_full_path

        dst_full_path = destination_path + file_name
        # print "dst_full_path:", dst_full_path

        #
        # Copy the file to the server
        #
        try:
            shutil.copyfile(src_full_path, dst_full_path)

        except Exception, e:

            return 0

        return 1

if __name__ == '__main__':

    print ">>> Running `FileUtility` module stand alone! <<<"

    FileUtility(debug=True)
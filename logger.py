# -*- coding: utf-8 -*-
import logging
import os
import dateTime

try:
    import __init__
except ImportError as err:
    print "ERROR >>> Could not import '__init__' <<<", err
    import __init__


__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"


class Logger:
    """
    When instantiating the Logger() class you should provide a log name.

    When logging you'll need to set the log level as such.

    log(0, "message")

    0 = debug
    1 = info
    2 = warn
    3 = error
    4 = critical
    """

    def __init__(self, debug=None):
        if debug: print "::Logger::__init__"

        self.debug = debug

        # Get date and time
        self.dt = dateTime.DateTime(debug=None)

        # Get global vars
        self.g = __init__.Globals()

    def create_logger(self, name=None):
        if self.debug: print "::Logger::create_logger"

        if name is None:
            name = "test_log"

        log_datetime = self.dt.get_datetime()
        # log_datetime = log_datetime[:8] + "_" + log_datetime[8:]
        log_datetime = log_datetime[:8]
        #print log_datetime

        ds = self.g.ds  # Directory Separator

        # Use the globals logs path
        if self.g.logs_path:
            log_folder = self.g.logs_path
        # if not, default to relative
        else:
            log_folder = "." + ds + "logs" + ds

        # Double check logs path has a dir separator
        #if log_folder[:-1] != ds:
        #    log_folder += ds

        #print "log_folder:", log_folder

        if not os.path.exists(log_folder):
            os.mkdir(log_folder)

        log_name = name+"_"+log_datetime+".log"
        if self.debug: print "log_name:", log_name

        self.log_full_path = log_folder + log_name
        if self.debug: print "log_full_path:", self.log_full_path

        # create logger
        logging.basicConfig(filename=self.log_full_path, level=logging.DEBUG,
                            format='%(asctime)s|%(levelname)s: %(message)s')  # %(name)s -

        #self.init_log()

    def init_log(self):
        if self.debug: print "::Logger::init_log"

        self.log(1, "")
        self.log(1, "----- Start Logging -----")

    def log(self, level, *msg):

        if len(msg) == 1:  # print msg
            msg = msg[0]

        else:
            messages = ""
            for i, m in enumerate(msg):
                # print i, m, type(m)

                if type(m) == dict:
                    messages += " " + self.convert_dict_to_str(m)

                elif type(m) == list:
                    messages += " " + self.convert_list_to_str(m)

                else:
                    messages += " " + str(m)

            msg = messages
            # print "	end msg", msg

        if level == 0:
            if self.debug: print "  debug:", msg
            logging.debug(msg)

        elif level == 1:
            if self.debug: print "  info:", msg
            logging.info(msg)

        elif level == 2:
            if self.debug: print "  warn:", msg
            logging.warn(msg)

        elif level == 3:
            if self.debug: print "  error:", msg
            logging.error(msg)

        elif level == 4:
            if self.debug: print "  critical:", msg
            logging.critical(msg)

        elif level == 99:
            if self.debug: print msg
            logging.info(msg)

    def convert_dict_to_str(self, dict_data, ident='', braces=1):
        message = ""
        for key, value in dict_data.iteritems():
            if isinstance(value, dict):
                message += '%s%s%s%s' % (ident, braces * '[', key, braces * ']')
                # self.convert_list_to_str(value, ident + '  ', braces+1)
                self.convert_dict_to_str(value, ident, braces + 1)
            else:
                message += ident + '%s = %s' % (key, value)
                # print message

        return message

    def convert_list_to_str(self, list_data):
        # print 'list:',list_data

        message = ""

        for l in list_data:

            if isinstance(l, list):
                # print "isinstance",l

                new_list = str(l)
                new_list = new_list.replace("[", "")
                new_list = new_list.replace("]", "")
                new_list = new_list.replace("\'", "")
                new_list = new_list.replace(",", "")
                new_list = new_list.replace(" ", "")

                message += ' ' + new_list

                self.convert_list_to_str(l);

            else:
                message += ' ' + ''.join(str(l))

        return message


if __name__ == "__main__":

    print ">>> Running `Logger` module stand alone! <<<"

    l = Logger(debug=True)
    l.create_logger('test_from_logger')
    l.init_log()
    l.log(1, "logging test...")

    #list_data = ['this', 'is', 'a', 'test', ['l','i','s','t'], 'today']
    #l.log(1, "list_data", list_data)
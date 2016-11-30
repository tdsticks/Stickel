# -*- coding: utf-8 -*-
import sys

import pymysql
from pymysql import err

try:
    import __init__
except ImportError:
    print "ERROR >>> Could not import __init__ <<<"
    import __init__

__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"


class DbConnection:

    def __init__(self, name, debug=False):

        self.debug = debug

        self._ = __init__

        self.g = self._.Globals(debug=None)

        # Start the logger
        self.l = self._.logger.Logger(debug=False)
        self.l.create_logger(name)
        self.l.init_log()

        self.l.log(1, "db_connection::__init__")

        self.user = ""
        self.pwd = ""

        if self.debug: print ">>> Local <<<"
        self.user = "Username here"
        self.pwd = "Password here"

        self.config = {
            'user': self.user,
            'password': self.pwd,
            'host': 'localhost',
            'database': 'Enter DB Name here',
            # 'charset': 'utf8',
            # 'collation': 'utf8_unicode_ci',
            # 'use_unicode': True,
            # 'raise_on_warnings': True,
            # 'connection_timeout': 600,
        }

        self.connect_db()

    def connect_db(self):

        # self.l.log(1, "db_connection::connect_db")

        try:
            self.cnx = pymysql.connect(**self.config)
            # print self.cnx

            self.cnx.autocommit(False)

        except err.ProgrammingError as e:
            self.l.log(3, "connect_db - ProgrammingError", e)
            raise

        except err.DataError as e:
            self.l.log(3, "connect_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "connect_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "connect_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "connect_db - OperationalError", e)
            raise

        except:
            self.l.log(3, "connect_db - Unexpected error:", sys.exc_info()[0])
            raise

    def select_all_db(self, query_str):
        #self.l.log(1, "db_connection::select_all_db")

        self.results = []

        self.cursor = self.cnx.cursor()

        try:

            if (query_str):

                #self.l.log(1, "query_str:", query_str)

                self.cursor.execute(query_str)

                rows = self.cursor.fetchall()

                for row in rows:
                    self.results.append(row)

        except err.ProgrammingError as e:
            self.l.log(3, "connect_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "select_all_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "select_all_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "select_all_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "select_all_db - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "select_all_db - Unexpected Error:", sys.exc_info()[0])
            raise

        return self.results

    def select_id_db(self, query_str):

        #self.l.log(1, "db_connection::select_db")

        self.results = ""

        self.cursor = self.cnx.cursor()

        try:

            if (query_str):
                self.cursor.execute(query_str)

                self.results = self.cursor.fetchone()
                # print "self.results", self.results

        except err.ProgrammingError as e:
            self.l.log(3, "select_id_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "select_id_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "select_id_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "select_id_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "select_id_db - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "select_id_db - Unexpected Error:", sys.exc_info()[0])
            raise

        return self.results

    def query_db(self, query_str):
        #self.l.log(1, "db_connection::query_db")

        self.results = ""
        self.cursor = self.cnx.cursor()

        try:

            if (query_str):

                # print "query_str", query_str

                self.results = self.cursor.execute(query_str)
                # print self.results

                qry_id = ""

                # Only return found records
                for id in self.cursor:

                    if id is not "":
                        qry_id = id

                        # Fix to get only value and not list
                        qry_id = qry_id[0]

                        return qry_id

        except err.ProgrammingError as e:
            self.l.log(3, "query_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "query_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "query_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "query_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "query_db - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "query_db - Unexpected Error:", sys.exc_info()[0])
            raise

        return self.results

    def insert_db(self, query_str):

        #self.l.log(1, "db_connection::insert_db")
        self.cursor = self.cnx.cursor()

        try:

            if (query_str):
                self.cursor.execute(query_str)
                # last_id 				= self.cursor.lastrowid
                # print "insert_db - last_id", last_id
                return True

        except err.ProgrammingError as e:
            self.l.log(3, "connect_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            # raise
            return False

        except err.DataError as e:
            self.l.log(3, "connect_db - DataError", e)
            self.dump_query("DataError", query_str)
            # raise
            return False

        except err.IntegrityError as e:
            self.l.log(3, "connect_db - IntegrityError", e)
            self.dump_query("IntegrityError", query_str)
            # raise
            return False

        except err.NotSupportedError as e:
            self.l.log(3, "connect_db - NotSupportedError", e)
            self.dump_query("NotSupportedError", query_str)
            # raise
            return False

        except err.OperationalError as e:
            self.l.log(3, "connect_db - OperationalError", e)
            self.dump_query("OperationalError", query_str)
            # raise
            return False

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            self.dump_query("InternalError", query_str)
            # raise
            return False

        except:
            self.l.log(3, "connect_db - Unexpected Error:", sys.exc_info()[0])
            self.dump_query("Unexpected Error", query_str)
            # raise
            return False

    def insert_w_return_db(self, query_str):

        #self.l.log(1, "db_connection::insert_w_return_db")
        self.cursor = self.cnx.cursor()

        try:

            if (query_str):
                self.cursor.execute(query_str)
                last_id = self.cursor.lastrowid
                # print "insert_db - last_id", last_id
                return last_id

            # return True
            else:
                return 0

        except err.ProgrammingError as e:
            self.l.log(3, "connect_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "connect_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "connect_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "connect_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "connect_db - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "connect_db - Unexpected Error:", sys.exc_info()[0])
            raise

    def insert_unique_db(self, table, field, value):

        #self.l.log(1, "db_connection::insert_unique_db")
        self.cursor = self.cnx.cursor()

        try:
            # Check to see if the entry exists first
            select_str = 'SELECT id FROM `%s` WHERE `%s` = "%s"' % (table, field, value)
            #self.l.log(1, "insert_unique_db - select_str", select_str)

            self.cursor.execute(select_str)

            select_id = self.cursor.fetchone()
            # print select_id, type(select_id)

            #self.l.log(1, "insert_unique_db - select_id", select_id)

            if select_id != None and select_id != 0:

                #self.l.log(1, "insert_unique_db - entry exists:", select_id[0], value)

                return select_id[0]

            else:
                # print "entry does not exist:", value

                insert_str = 'INSERT INTO `%s` (`%s`) VALUES ("%s")' % (table, field, value)
                #self.l.log(1, "insert_unique_db - insert_str", insert_str)

                self.cursor.execute(insert_str)

                return self.cursor.lastrowid

        except err.ProgrammingError as e:
            self.l.log(3, "insert_unique_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "insert_unique_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "insert_unique_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "insert_unique_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "insert_unique_db - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "insert_unique_db - Unexpected Error:", sys.exc_info()[0])
            raise

    def insert_unique_db_error(self, table, field, value):

        #self.l.log(1, "db_connection::insert_unique_db")
        self.cursor = self.cnx.cursor()

        try:
            # Check to see if the entry exists first
            select_str = 'SELECT id FROM `%s` WHERE `%s` = "%s"' % (table, field, value)
            # print "select_str", select_str

            #self.l.log(1, "insert_unique_db - select_str", select_str)

            self.cursor.execute(select_str)

            select_id = self.cursor.fetchone()
            # print select_id, type(select_id)

            #self.l.log(1, "insert_unique_db - select_id", select_id)

            if select_id != None or select_id != 0:
                # print "entry exists:",select_id[0], value

                return False

            else:
                # print "entry does not exist:", value

                insert_str = 'INSERT INTO `%s` (`%s`) VALUES ("%s")' % (table, field, value)
                # print "insert_str", insert_str

                self.cursor.execute(insert_str)

                return self.cursor.lastrowid

        except err.ProgrammingError as e:
            self.l.log(3, "insert_unique_db_error - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "insert_unique_db_error - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "insert_unique_db_error - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "insert_unique_db_error - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "insert_unique_db_error - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "insert_unique_db_error - Unexpected Error:", sys.exc_info()[0])
            self.dump_query('Unexpected Error'.sys.exc_info()[0], select_str)
            raise

    def update_db(self, query_str):

        #self.l.log(1, "db_connection::update_db")

        self.results = ""
        self.cursor = self.cnx.cursor()

        try:
            if (query_str):
                # print "query_str", query_str

                self.results = self.cursor.execute(query_str)
                # print self.results

        except err.ProgrammingError as e:
            self.l.log(3, "update_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "update_db - DataError", e)
            self.dump_query("DataError", query_str)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "update_db - IntegrityError", e)
            self.dump_query("IntegrityError", query_str)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "update_db - NotSupportedError", e)
            self.dump_query("NotSupportedError", query_str)
            raise

        except err.OperationalError as e:
            self.l.log(3, "update_db - OperationalError", e)
            self.dump_query("OperationalError", query_str)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            self.dump_query("InternalError", query_str)
            raise

        except:
            self.l.log(3, "update_db - Unexpected Error:", sys.exc_info()[0])
            self.dump_query("Unexpected Error", query_str)
            raise

        return self.results

    def truncate_db(self, table):

        #self.l.log(1, "db_connection::truncate_db")

        self.results = ""
        self.cursor = self.cnx.cursor()

        try:

            if (table):
                truncate_str = 'TRUNCATE `%s`' % (table)
                # print "truncate_str", truncate_str

                self.results = self.cursor.execute(truncate_str)
                # print self.results

        except err.ProgrammingError as e:
            self.l.log(3, "truncate_db - ProgrammingError", e)
            self.dump_query("ProgrammingError", query_str)
            raise

        except err.DataError as e:
            self.l.log(3, "truncate_db - DataError", e)
            raise

        except err.IntegrityError as e:
            self.l.log(3, "truncate_db - IntegrityError", e)
            raise

        except err.NotSupportedError as e:
            self.l.log(3, "truncate_db - NotSupportedError", e)
            raise

        except err.OperationalError as e:
            self.l.log(3, "truncate_db - OperationalError", e)
            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            raise

        except:
            self.l.log(3, "truncate_db - Unexpected Error:", sys.exc_info()[0])
            raise

        return self.results

    def connection_commit(self):
        # self.l.log(1, "db_connection::connection_commit")

        try:
            self.cnx.commit()

        except err.ProgrammingError as e:
            self.l.log(3, "connection_commit - ProgrammingError", e)
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

        except err.DataError as e:
            self.l.log(3, "connection_commit - DataError", e)
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

        except err.IntegrityError as e:
            self.l.log(3, "connection_commit - IntegrityError", e)
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

        except err.NotSupportedError as e:
            self.l.log(3, "connection_commit - NotSupportedError", e)
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

        except err.OperationalError as e:
            self.l.log(3, "connection_commit - OperationalError", e)
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

        except err.InternalError as e:
            self.l.log(3, "select_all_db - InternalError", e)
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

        except:
            self.l.log(3, "connection_commit - Unexpected Error:", sys.exc_info()[0])
            self.cnx.rollback()
            self.l.log(3, "something failed with the commit, rolling back...")

            raise

    def cursor_close(self):
        # self.l.log(1, "db_connection::cursor_close")

        if self.cursor:

            try:
                self.cursor.close()

            except err.ProgrammingError as e:
                self.l.log(3, "cursor_close - ProgrammingError", e)
                raise

            except err.DataError as e:
                self.l.log(3, "cursor_close - DataError", e)
                raise

            except err.IntegrityError as e:
                self.l.log(3, "cursor_close - IntegrityError", e)
                raise

            except err.NotSupportedError as e:
                self.l.log(3, "cursor_close - NotSupportedError", e)
                raise

            except err.OperationalError as e:
                self.l.log(3, "cursor_close - OperationalError", e)
                raise

            except err.InternalError as e:
                self.l.log(3, "select_all_db - InternalError", e)
                raise

            except:
                self.l.log(3, "cursor_close - Unexpected Error:", sys.exc_info()[0])
                raise

    def connection_close(self):
        # self.l.log(1, "db_connection::connection_close")

        self.cnx.close()

    def dump_query(self, err_type, query):
        self.l.log(1, "db_connection::dump_query")

        self.l.log(3, "\nDB ERROR - pymysql - error type:", err_type)

        self.l.log(3, "*******************************************")
        self.l.log(3, "DB ERROR with query: " + query)
        self.l.log(3, "*******************************************")


if __name__ == '__main__':

    print ">>> Running `DbConnection` module stand alone! <<<"

    DbConnection('test', debug=True)

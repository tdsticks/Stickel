# -*- coding: utf-8 -*-
import smtplib
from logger import Logger

__author__ = 'Steve Stickel'
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__maintainer__ = "Steve Stickel"
__email__ = "tdsticks@gmail.com"

'''
How to Enable Local SMTP (Postfix) on OS-X
    http://apple.stackexchange.com/questions/32228/whats-the-correctly-way-to-make-postfix-run-permanently-on-lion-not-server
    http://sunzhen.blogspot.com/2011/11/how-to-enable-local-smtp-postfix-on-os.html
    sudo postfix start
    sudo postfix stop
'''


class Email:

    def __init__(self, name):
        #print "Email::__init__"

        # Instantiate the logging
        logger = Logger(name)
        self.log = logger.log

        self.raw_datetime = logger.todays_datetime

        self.log(1, "Email::__init__")

        #
        # Sender
        #
        self.sender = 'test@python.com'
        self.from_sender = "test email " + "<" + self.sender + ">"

        #
        # Recipients
        #
        self.receivers_dev = ['tdsticks@gmail.com']
        self.to_dev_recipients = "Steve Stickel" + "<" + self.receivers_dev[0] + ">"

        self.server = "localhost"
        self.port = 25

    def format_email_body(self, list_title, data_list):

        self.log(1, "Email::format_email_msg")

        self.body += "\n<b>%s</b>\n" % list_title

        self.body += "<ul>"

        #
        # Loop through the data
        #
        for data in data_list:
            self.body += "<li>%s</li>" % (data)

        self.body += "</ul>"

    def format_datetime(self):

        self.log(1, "Email::format_datetime")

        rdt = self.raw_datetime
        # print "rdt", rdt

        formatted_datetime = rdt[0:4] + "-" + rdt[4:6] + "-" + rdt[6:8] + " " + rdt[8:10] + ":" + rdt[10:12] + ":" + rdt[12:14]
        # print "formatted_datetime", formatted_datetime

        return formatted_datetime

    def create_html_mail(self, html, text, subject, from_sender, to_recipients, cc_recipients):

        # self.log( 1, "Email::create_html_mail" )

        #
        # Create a mime-message that will render HTML in popular
        # MUAs, text in better ones
        #
        import MimeWriter
        import mimetools
        import cStringIO

        out = cStringIO.StringIO()  # output buffer for our message
        htmlin = cStringIO.StringIO(html)
        txtin = cStringIO.StringIO(text)
        writer = MimeWriter.MimeWriter(out)

        #
        # set up some basic headers... we put subject here
        # because smtplib.sendmail expects it to be in the
        # message body
        #
        writer.addheader("From", from_sender)
        writer.addheader("To", to_recipients)

        # Add CC if there is data
        if len(cc_recipients) > 0:
            writer.addheader("CC", cc_recipients)

        writer.addheader("Subject", subject)
        writer.addheader("MIME-Version", "1.0")

        #
        # start the multipart section of the message
        # multipart/alternative seems to work better
        # on some MUAs than multipart/mixed
        #
        writer.startmultipartbody("alternative")
        writer.flushheaders()

        #
        # the plain text section
        #
        subpart = writer.nextpart()
        subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
        pout = subpart.startbody("text/plain", [("charset", 'us-ascii')])
        mimetools.encode(txtin, pout, 'quoted-printable')
        txtin.close()

        #
        # start the html subpart of the message
        #
        subpart = writer.nextpart()
        subpart.addheader("Content-Transfer-Encoding", "quoted-printable")

        #
        # returns us a file-ish object we can write to
        #
        pout = subpart.startbody("text/html", [("charset", 'us-ascii')])
        mimetools.encode(htmlin, pout, 'quoted-printable')
        htmlin.close()

        #
        # Now that we're done, close our writer and
        # return the message body
        #
        writer.lastpart()
        msg = out.getvalue()
        out.close()

        # print msg
        return msg

    def send(self, sub='', body=''):

        self.log(1, "Email::send")

        self.sub = sub
        self.body = body

        if self.sub == '':
            self.sub = "Test from Python"

        if self.body == '':
            self.body = "This is a message from Python"

        self.log(1, "Email Subject: ", self.sub)
        # self.log( 1, "Email Body: ", self.body )

        html = self.body.replace("\n", "<br/>")
        text = self.body

        # message = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % \
        #           ( self.sender, self.receivers[0], self.sub, self.body )
        # print "message", message

        message = self.create_html_mail(html, text, self.sub, self.from_sender, self.to_dev_recipients, "")
        # self.log( 1, "Email Message: ", message )

        # message += "From: " + from_sender + " <" + self.sender + ">"
        # self.log( 1, "Email Message: ", message )

        server = smtplib.SMTP(self.server, self.port)
        # server = smtplib.SMTP( server )
        # print "server", server

        server.sendmail(self.sender, self.receivers_dev, message)
        server.quit()

        # print server
        print "email sent!"

        self.log(1, "Email sent to: ", self.receivers_dev)


if __name__ == '__main__':

    email = Email("email_test")
    email.send("Email Test", "This is an email test")


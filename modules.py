from email.message import EmailMessage
import smtplib
from datetime import datetime
import imaplib
from email.parser import HeaderParser
from email.utils import parsedate_tz, mktime_tz
import re


def get_age_of_newest_mail_with_pattern(user, password, imap_url, match_pattern="Test Message"):
    M = imaplib.IMAP4_SSL(imap_url)
    M.login(user, password)

    M.select("INBOX")
    (retcode, messages) = M.search(None, 'ALL')

    ids = messages[0]
    id_list = ids.split()
    latest_ten_email_id = id_list[-10:]
    keys = map(int, latest_ten_email_id)
    news_keys = sorted(keys, reverse=True)
    news_mail = [str(e) for e in news_keys]
    if len(news_mail) == 0:
        raise Exception("Inbox is Empty")

    newest_date = None
    for i in news_mail:
        data = M.fetch(i, '(BODY[HEADER])')
        header_data = data[1][0][1]
        parser = HeaderParser()
        msg = parser.parsestr(header_data.decode("utf-8"))
        date = msg["Date"]
        ts = mktime_tz(parsedate_tz(date))
        date_ts = datetime.fromtimestamp(ts)
        pattern = re.compile(match_pattern)
        if pattern.match(msg['Subject']):
            if newest_date is None or newest_date < date_ts:
                newest_date = date_ts
    if newest_date is None:
        raise Exception("pattern '{}' not found in Inbox".format(match_pattern))
    delta= datetime.now() -  newest_date
    return delta.seconds


def send_smtp_mail(mail_from, mail_to, subject, message, smtp_host, password, port=587):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = [mail_to]
    with smtplib.SMTP(smtp_host, port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(mail_from, password)
        smtp.send_message(msg, mail_from, mail_to)

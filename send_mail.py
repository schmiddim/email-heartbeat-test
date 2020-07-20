from modules import send_smtp_mail
from os import getenv

smtp_server = getenv('SMTP_HOST')
user = getenv('SENDER_USER')
password = getenv('SENDER_PASSWORD')
port = getenv('SMTP_PORT')

send_smtp_mail(mail_from=user,
               mail_to=user,
               subject=getenv('SEND_SUBJECT'),
               message=getenv('SEND_MESSAGE'),
               smtp_host=smtp_server,
               password=password,
               port=587
               )

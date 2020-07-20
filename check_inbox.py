from modules import get_age_of_newest_mail_with_pattern

from os import getenv

imap_url = getenv('IMAP_HOST')
user = getenv('USER')
password = getenv('PASSWORD')
threshold_seconds = int(getenv('TRESHHOLD_SECONDS'))
result = get_age_of_newest_mail_with_pattern(user=user,
                                             password=password,
                                             imap_url=imap_url,
                                             match_pattern='Test Message'
                                             )

if result > threshold_seconds:
    raise Exception('Age of last message above threshold: {}'.format(result))

print('Age of last message: {}'.format(result))

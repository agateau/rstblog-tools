import sys
import time

from datetime import datetime

BREAK = '<!-- break -->'


def tzstring():
    delta = time.timezone
    dt = datetime.utcfromtimestamp(abs(delta))
    txt = dt.strftime('%H:%M')
    if delta > 0:
        return '-' + txt
    else:
        return '+' + txt


def get_date():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S') + ' ' + tzstring()


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def confirm(prompt):
    answer = input(prompt + ' [yN] ')
    if not answer:
        return False
    return answer[0].lower() == 'y'

import sys

BREAK = '<!-- break -->'


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def confirm(prompt):
    answer = input(prompt + ' [yN] ')
    if not answer:
        return False
    return answer[0].lower() == 'y'

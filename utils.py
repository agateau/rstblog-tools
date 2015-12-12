import sys


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

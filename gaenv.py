from clime.core import Command
from clime.core import Program

import sys


def parse(sdk, path):
    print sdk


def cmd_main():
    parse_command = Command(parse)
    parse_command.execute(' '.join(sys.argv[1:]))

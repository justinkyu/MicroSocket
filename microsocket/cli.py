import sys

from .core import connect

HELP = """
MicroSocket v0.1

Usage

python3 -m microsocket <host> <port>

Example

python3 -m microsocket google.com 443
"""

def main():

    args = sys.argv[1:]

    if len(args) != 2:
        print(HELP)
        return

    connect(args[0], args[1])

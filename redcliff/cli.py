from sys import exit

import argparse

from .config import get_config
from .commands import dispatch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--base-url')
    parser.add_argument('-k', '--api-key')
    parser.add_argument('-C', '--config-file')
    parser.add_argument('cmd')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    conf = get_config(args.config_file)
    return dispatch(args.cmd, args.args, conf)


if __name__ == '__main__':
    exit(main())

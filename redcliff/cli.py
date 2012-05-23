from sys import exit

import argparse

from .commands import dispatch
from .config import get_config
from .utils import merge


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--base-url')
    parser.add_argument('-k', '--api-key')
    parser.add_argument('-C', '--config-file')
    parser.add_argument('cmd')
    parser.add_argument('args', nargs=argparse.REMAINDER)

    args = vars(parser.parse_args())
    conf = get_config(args.pop('config_file'))

    cmd = args.pop('cmd')
    cmd_args = args.pop('args')
    merged_conf = merge(conf, args)

    return dispatch(cmd, cmd_args, merged_conf)


if __name__ == '__main__':
    exit(main())

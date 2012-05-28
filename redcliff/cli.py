from sys import exit

import argparse

from .commands import dispatch, choices
from .config import get_config
from .utils import merge, error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--base-url',
                        dest='url',
                        metavar='https://redmine.example.com',
                        help='Base URL of your Redmine installation.')
    parser.add_argument('-S', '--no-ssl-verify', dest='ssl_verify',
                        action='store_const', const=False)
    parser.add_argument('-k', '--api-key',
                        dest='key',
                        help='Your Redmine API key.')
    parser.add_argument('-C', '--config-file',
                        help='Override default config path.')
    parser.add_argument('cmd',
                        choices=choices,
                        help='Command to execute.')
    parser.add_argument('args',
                        nargs=argparse.REMAINDER,
                        help='Arguments to command. Use --help to get '
                             'command-specific help.')

    args = vars(parser.parse_args())
    conf = get_config(args.pop('config_file'))

    cmd = args.pop('cmd')
    cmd_args = args.pop('args')
    merged_conf = merge(conf, args)

    required = ['url', 'key']
    missing = lambda x: bool(merged_conf.get(x))
    if not all(map(missing, required)):
        error('fatal: base_url and api_key are required')
        return 1

    return dispatch(cmd, cmd_args, merged_conf)


if __name__ == '__main__':
    exit(main())

import argparse

from ..utils import error
from .. import api


def run(argv, conf):
    parser = argparse.ArgumentParser(prog='list')
    parser.add_argument('-l', '--limit',
                        type=int,
                        metavar='NUM',
                        help='Limit the number of issues.')
    parser.add_argument('-o', '--offset',
                        type=int,
                        metavar='NUM',
                        help='Pagination offset.')
    parser.add_argument('-m', '--for-me',
                        action='store_const', const=True,
                        help='Show only issues assigned to me.')
    parser.add_argument('-a', '--assignee',
                        type=int,
                        dest='assigned_to_id',
                        metavar='ID',
                        help='Filter issues by "assigned to" field.')
    parser.add_argument('-p', '--project',
                        dest='project_id',
                        metavar='ID|name',
                        help='Filter issues by project. Might be project ID or'
                             ' identifier.')
    args = vars(parser.parse_args(argv))

    if args['for_me'] and not args['assigned_to_id']:
        user = api.users.current(None, conf)
        args['assigned_to_id'] = user['id']

    try:
        data = api.issues.list(args, conf)
    except api.AuthError:
        error('fatal: authentication error')
        return 1
    except:
        error('fatal: API error')
        raise
    else:
        print(data)
    return 0

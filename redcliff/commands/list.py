import argparse

from .. import api
from .. import renderer
from ..utils import error


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
    parser.add_argument('-s', '--status',
                        help='Filter issues by status.')
    args = vars(parser.parse_args(argv))

    if args['for_me'] and not args['assigned_to_id']:
        user = api.users.current(None, conf)
        args['assigned_to_id'] = user['id']
    if args['status']:
        status = api.statuses.by_name(args['status'], conf)
        if status:
            args['status_id'] = status['id']
        else:
            error('error: status {0} not found'.format(args['status']))

    try:
        data = api.issues.list(args, conf)
    except:
        error('fatal: API error while gettings issues list')
        raise
    else:
        renderer.issues.as_table(data)
    return 0

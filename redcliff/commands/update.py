import argparse

from .. import api
from ..utils import error, success


def run(argv, conf):
    parser = argparse.ArgumentParser(prog='update')
    parser.add_argument('-s', '--status',
                        help='Change issue status.')
    parser.add_argument('id',
                        type=int)
    args = vars(parser.parse_args(argv))

    if args['status']:
        status = api.statuses.by_name(args.pop('status'), conf)
        if status:
            args['status_id'] = status['id']
        else:
            error('fatal: status {0} not found'.format(args['status']))
            return 1

    try:
        api.issues.update(args, conf)
    except api.AuthError:
        error('fatal: authentication error')
        return 1
    except:
        error('fatal: API error')
        raise
    else:
        success('Successfully updated.')
    return 0

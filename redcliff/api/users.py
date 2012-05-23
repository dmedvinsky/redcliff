from . import Redmine


def current(args, conf):
    response = Redmine(conf).get('users/current')
    return response.json['user']

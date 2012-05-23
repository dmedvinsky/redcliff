from . import Redmine, AuthError


def list(args, conf):
    response = Redmine(conf).get('issue_statuses', None)
    if response.status_code == 401:
        raise AuthError
    return response.json


def by_name(name, conf):
    statuses = list(None, conf)['issue_statuses']
    matched = [s for s in statuses if s['name'] == name]
    return matched[0] if matched else None

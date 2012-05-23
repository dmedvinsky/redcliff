from . import Redmine, AuthError


def list(args, conf):
    response = Redmine(conf).get('issues', args)
    if response.status_code == 401:
        raise AuthError
    return response.json

import json

import requests


class AuthError(Exception):
    pass


class Redmine(object):
    def __init__(self, conf):
        url = conf['url']
        self.url = url[:-1] if url.endswith('/') else url
        self.ssl_verify = conf['ssl_verify']
        self.key = conf['key']
        self.headers = {'X-Redmine-API-Key': self.key,
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    def get(self, resource, params=None):
        url = '%s/%s.json' % (self.url, resource)
        response = requests.get(url,
                                verify=self.ssl_verify,
                                headers=self.headers,
                                params=params)
        if response.status_code == 401:
            raise AuthError
        return response

    def put(self, resource, data=None):
        url = '%s/%s.json' % (self.url, resource)
        response = requests.put(url,
                                verify=self.ssl_verify,
                                headers=self.headers,
                                data=json.dumps(data))
        if response.status_code == 401:
            raise AuthError
        return response


from . import issues, users, statuses
__all__ = [AuthError, issues, users, statuses]

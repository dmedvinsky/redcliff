from . import Redmine


def list(args, conf):
    response = Redmine(conf).get('issues', args)
    return response.json


def update(args, conf):
    id = args.pop('id')
    data = {'issue': args}
    response = Redmine(conf).put('issues/{0}'.format(id), data)
    return response.json

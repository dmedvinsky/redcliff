from importlib import import_module

from ..utils import error


choices = ['list', 'forme', 'now', 'update', 'fix', 'close']


def dispatch(cmd, args, conf):
    modules = dict((n, import_module('.%s' % n, __name__)) for n in choices)
    try:
        run = modules[cmd].run
    except (KeyError, AttributeError):
        error('fatal: invalid command {0}'.format(cmd))
        return 1
    return run(args, conf)

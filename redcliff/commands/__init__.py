from ..utils import error


choices = ['list', 'forme', 'now']


def dispatch(cmd, args, conf):
    from . import list, forme, now  # NOQA
    try:
        run = locals()[cmd].run
    except (KeyError, AttributeError):
        error('fatal: invalid command {0}'.format(cmd))
        return 1
    return run(args, conf)

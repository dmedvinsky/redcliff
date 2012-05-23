from clint import textui as ui


def dispatch(cmd, args, conf):
    from . import list  # NOQA
    try:
        return locals()[cmd].run(args, conf)
    except (KeyError, AttributeError):
        ui.puts(ui.colored.red('fatal: invalid command {0}'.format(cmd)),
                stream=ui.STDERR)
        return 1

from importlib import import_module

from clint import textui as ui


def dispatch(cmd, args, conf):
    try:
        command = import_module('.{0}'.format(cmd), __name__)
        return command.run(args, conf)
    except (ImportError, AttributeError):
        ui.puts(ui.colored.red('fatal: invalid command {0}'.format(cmd)),
                stream=ui.STDERR)
        return 1

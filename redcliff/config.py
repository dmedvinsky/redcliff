import json

from clint import resources
from clint import textui as ui

from .utils import compose, merge


defaults = lambda: {

}


def open_config(path):
    if path is None:
        resources.init('Universe', 'redcliff')
        return resources.user.open('config.json', 'r')
    else:
        return open(path, 'r')


def read(path):
    try:
        with open_config(path) as f:
            return f.read()
    except IOError:
        return ''


def get_config(path):
    try:
        conf = parse_file(path)
    except ValueError:
        ui.puts(ui.colored.red("error: couldn't parse config file"),
                stream=ui.STDERR)
        conf = {}
    return merge(conf, defaults())


parse = json.loads
parse_file = compose(parse, read)


__all__ = [get_config, parse_file]

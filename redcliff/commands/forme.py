from . import list


def run(argv, conf):
    argv.append('--for-me')
    return list.run(argv, conf)

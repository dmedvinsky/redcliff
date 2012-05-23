from . import update


def run(argv, conf):
    argv.append('--status')
    argv.append('Fixed')
    return update.run(argv, conf)

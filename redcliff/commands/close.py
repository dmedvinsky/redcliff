from . import update


def run(argv, conf):
    argv.append('--status')
    argv.append('Closed')
    return update.run(argv, conf)

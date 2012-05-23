from functools import reduce, wraps
from itertools import chain

from clint import textui as ui


compose = lambda *fs: reduce(lambda f, g: lambda *a, **ka: f(g(*a, **ka)), fs)
merge = lambda d1, d2: dict(chain([i for i in d1.items() if i[1] is not None],
                                  [i for i in d2.items() if i[1] is not None]))
error = lambda x: ui.puts(ui.colored.red(x), stream=ui.STDERR)
success = lambda x: ui.puts(ui.colored.green(x), stream=ui.STDOUT)


def flip(f):
    @wraps(f)
    def g(*args, **kwargs):
        return f(*reversed(args), **kwargs)
    return g


__all__ = [compose, flip, merge]

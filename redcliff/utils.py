from functools import reduce, wraps
from itertools import chain


compose = lambda *fs: reduce(lambda f, g: lambda *a, **ka: f(g(*a, **ka)), fs)
merge = lambda d1, d2: dict(chain([i for i in d1.items() if i[1] is not None],
                                  [i for i in d2.items() if i[1] is not None]))


def flip(f):
    @wraps(f)
    def g(*args, **kwargs):
        return f(*reversed(args), **kwargs)
    return g


__all__ = [compose, flip, merge]

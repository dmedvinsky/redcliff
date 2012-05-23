from functools import reduce, wraps
from itertools import chain


compose = lambda *fs: reduce(lambda f, g: lambda *a, **ka: f(g(*a, **ka)), fs)
merge = lambda d1, d2: dict(chain(d1.items(), d2.items()))


def flip(f):
    @wraps(f)
    def g(*args, **kwargs):
        return f(*reversed(args), **kwargs)
    return g


__all__ = [compose, flip, merge]

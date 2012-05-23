from functools import reduce, wraps


compose = lambda *fs: reduce(lambda f, g: lambda *a, **ka: f(g(*a, **ka)), fs)


def flip(f):
    @wraps(f)
    def g(*args, **kwargs):
        return f(*reversed(args), **kwargs)
    return g


__all__ = ['compose', 'flip']

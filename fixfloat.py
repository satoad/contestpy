def fix(n):
    def decor(func):
        def nfun(*args, **kwargs):
            kwargs = {key: round(value, n) for (key, value) in kwargs.items()}
            return func(*list(map(lambda x: x if not isinstance(x, float) else round(x, n), args)), **kwargs)
        return nfun
    return decor

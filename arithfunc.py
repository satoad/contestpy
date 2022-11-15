def ADD(f, g):
    def function(x):
        if callable(f):
            if callable(g):
                return f(x) + g(x)
            else:
                return f(x) + g
        elif callable(g):
            return f + g(x)
        else:
            return f + g
    return function

def SUB(f, g):
    def function(x):
        if callable(f):
            if callable(g):
                return f(x) - g(x)
            else:
                return f(x) - g
        elif callable(g):
            return f - g(x)
        else:
            return f - g
    return function

def MUL(f, g):
    def function(x):
        if callable(f):
            if callable(g):
                return f(x) * g(x)
            else:
                return f(x) * g
        elif callable(g):
            return f * g(x)
        else:
            return g * f
    return function

def DIV(f, g):
    def function(x):
        if callable(f):
            if callable(g):
                return f(x) / g(x)
            else:
                return f(x) / g
        elif callable(g):
            return f / g(x)
        else:
            return g / f
    return function

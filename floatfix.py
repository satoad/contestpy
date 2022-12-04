import types
import numbers

def decor(fun, arg):
    def new_f(*args, **kwargs):
        res = fun(*args, **kwargs)
        if isinstance(res, numbers.Real):
            return round(res, arg)
        else:
            return res
    return new_f

class fixed(type):
    def __new__(cls, clsname, bases, attrs, **kwds):
        par = 3
        if 'ndigits' in kwds.keys():
             par = kwds['ndigits']
            
        new_attrs = {}
        for attr, v in attrs.items():
            if not isinstance(v, types.FunctionType):
                new_attrs[attr] = v
            else:
                new_attrs[attr] = decor(v, par)
        return type(clsname, bases, new_attrs)
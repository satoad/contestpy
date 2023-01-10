import inspect
import types
import numbers
from typing import Callable

def dec(fun):
    def new_f(*args, **kwargs):
        if fun.__defaults__ is not None:
            for i in list(inspect.signature(fun).parameters.values())[len(args):-1]:
                if str(i).split()[0].split(':')[0] not in fun.__defaults__:
                    if str(i).split()[0].split(':')[0] not in kwargs and str(i) != 'self':
                        if type(i.annotation) == types.GenericAlias:
                            kwargs[str(i).split()[0].split(':')[0]] = i.annotation.__origin__()
                        else:
                            try:
                                kwargs[str(i).split()[0].split(':')[0]] = i.annotation()
                            except Exception:
                                kwargs[str(i).split()[0].split(':')[0]] = None
        else:
            for i in list(inspect.signature(fun).parameters.values())[len(args):]:
                if str(i).split()[0].split(':')[0] not in kwargs and str(i) != 'self':
                    if type(i.annotation) == types.GenericAlias:
                        kwargs[str(i).split()[0].split(':')[0]] = i.annotation.__origin__()
                    else:
                        try:
                            kwargs[str(i).split()[0].split(':')[0]] = i.annotation()
                        except Exception:
                               kwargs[str(i).split()[0].split(':')[0]] = None


        return fun(*args, **kwargs)
    return new_f


class init(type):
    def __new__(cls, clsname, bases, attrs, **kwds):
        for attr, v in attrs.items():
            if isinstance(v, Callable):
                attrs[attr] = dec(v)
        return super().__new__(cls, clsname, bases, attrs)

class Nuts:
    __delitem__ = __setitem__ = __setattr__ = __delattr__ = __init__ = lambda self, *other: None
    __str__ = __getattribute__ = __getitem__ = lambda self, item=None: item if item is not None else type(self).__name__
    __iter__ = lambda self: iter("Nuts")
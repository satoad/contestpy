def sloter(fields, defaults):

    class ncls:
        __slots__ = fields

        def __init__(self):
            for i in fields:
                self.__setattr__(i, defaults)

        def __delattr__(self, item):
            self.__setattr__(item, defaults)

        def __iter__(self):
            return iter(list(self.__getattribute__(i) for i in self.__slots__))

    return ncls
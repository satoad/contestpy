from itertools import tee
from itertools import zip_longest

def seesaw(sequense):
    iter1, iter2 = tee(sequense)

    even = []
    odd = []
    for i in iter1:
        if i % 2 == 0:
            even.append(i)

    for i in iter2:
        if i % 2 != 0:
            odd.append(i)

    res = zip_longest(even, odd)
    for i in res:
        if i[0] != None and i[1] != None:
            yield i[0]
            yield i[1]
        elif i[0]:
            yield i[0]
        elif i[1]:
            yield i[1]
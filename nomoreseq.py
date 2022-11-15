def nomore(sequense):
    j = 0

    for j in sequense:
        for i in sequense:
            if i <= j:
                yield i
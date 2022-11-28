def statcounter():
    stats = {}
    res = yield stats

    while True:
        stats[res] = 0
        def decor(f):
            def newf(*args):
                if f in stats.keys():
                    stats[f] += 1
                else:
                    stats[f] = 1
                return f(*args)
            return newf
        res = yield decor(res)
def No_2Zero(n, k):
    def f(n):
        tmp = k - 1
        if n == 2:
            return k * tmp
        elif n >= 2:
            return tmp * f(n-1) + tmp * f(n-2)
        return tmp
    return f(n)
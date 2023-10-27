import math
import decimal


def PiGen():
    decimal.getcontext().prec = 9999
    numerator = 426880 * decimal.Decimal(10005).sqrt()
    series_sum = decimal.Decimal(0)
    k = 0
    while True:
        series_sum += math.factorial(6 * k) * (545140134 * k + 13591409) \
                      / (math.factorial(3 * k) * math.factorial(k) ** 3 * decimal.Decimal(-262537412640768000) ** k)
        k += 1
        yield numerator / series_sum



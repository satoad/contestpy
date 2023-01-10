k = eval(input())
i = 1
d = 10 * k
while True:
    a = k * (10 ** i - 1)
    if a % (d - 1) == 0:
        print(a // (d - 1))
        break
    i += 1

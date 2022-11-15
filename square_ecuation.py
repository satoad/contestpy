import math 

a, b, c = eval(input())

if a == 0:
    if c != 0:
        print(c / b)
    else:
        print(-1)
else:
    d = b**2 - 4 * a * c
    if d == 0:
        print(-(b / (2 * a)))
    elif d < 0:
        print(0)
    else:
        x1 = (((-b) + math.sqrt(d)) / (2 * a))
        x2 = (((-b) - math.sqrt(d)) / (2 * a))

        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)

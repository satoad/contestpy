import decimal

func = input()
context = eval(input())

decimal.getcontext().prec = context + 2
left, right = decimal.Decimal(-1.5), decimal.Decimal(1.5)

length = lambda x, y: x - y

sign = eval(func, {"x": left})
flag = False

while (right + left) / 2 != left and (right + left) / 2 != right:
    y = eval(func, {"x": (left + right) / 2})

    if y * sign < 0:
        right = (left + right) / 2
    elif y * sign > 0:
        left = (left + right) / 2
    elif y == 0:
        print(str("{:." + str(context) + "f}").format((left + right) / 2))
        flag = True
        break

if not flag:
    print(str("{:." + str(context) + "f}").format(right))
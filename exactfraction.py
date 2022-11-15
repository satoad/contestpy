from fractions import Fraction

a = input().replace(" ", "")

const = 'Fraction("'
i = 0
n = len(a)
while i < n:
    if a[i] == '.':
        left = i - 1
        while left >= 0 and a[left] <= '9' and a[left] >= '0':
            left -= 1

        right = i + 1
        while len(a) > right and a[right] <= '9' and a[right] >= '0':
            right += 1

        a = a[:left + 1] + const + a[left + 1:right] + '")' + a[right:]

        i = right + len(const)
        n = len(a)

    elif a[i] <= '9' and a[i] >= '0':
        left = i - 1
        while left >= 0 and a[left] <= '9' and a[left] >= '0':
            left -= 1

        right = i + 1
        while len(a) > right and a[right] <= '9' and a[right] >= '0':
            right += 1

        if right >= len(a):
            a = a[:left + 1] + const + a[left + 1:] + '")'
            break

        if a[right] == '.':
            i += 1
            continue

        a = a[:left + 1] + const + a[left + 1:right] + '")' + a[right:]

        i = right + len(const)
        n = len(a)
    else:
        i += 1

print(eval(a))
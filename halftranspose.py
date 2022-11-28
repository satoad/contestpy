a = []
b = input()
a.append([i for i in b.split(',')])

count = len(b.split(','))
for _ in range(count - 1):
    a.append([i for i in input().split(',')])

n = len(a)
flag = False
for i in range(0, n):
    for j in range(i + 1):
        print(a[i][j],end='')
        if j != i + 1 and flag:
            print(',', end='')
        elif not flag:
            flag = True
    for j in range(i - 1, -1, -1):
        print(a[j][i], end = '')
        if j != 0:
            print(',', end='')
    print()

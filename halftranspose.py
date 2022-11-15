a = []

b = input()
print(b)
a.append([i for i in b.split(',')])
n = len(a)
print(n)

for j in range(n - 1):
    b = input()
    a.append([i for i in b.split(',')])

n = len(a)
for i in range(n):
    for j in range(i + 1):
        print(a[i][j],end='')
        if(j != i + 1):
            print(',', end='')
    for j in range(i - 1, -1, -1):
        print(a[j][i], end = '')
        if(j != 0):
            print(',', end='')
    print()
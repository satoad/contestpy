def time_format(time):
    parts = time.split(":")
    new_time = 0

    dec = 4
    for i in parts:
        new_time += int(i) * 10**dec
        dec -= 2

    return new_time

a = []

while b := input():
    tmp = b.split()
    tmp[2:-1] = [' '.join(tmp[2:-1])]

    a.append(tmp)

b = sorted(a, key=lambda one: (time_format(one[-1]), one[1], one[0], one[2]))

count = 1
if len(b) > 3:
    count = 3

uniq_time = 1
for i in range(0, len(b) - 1):
    if time_format(b[i][3]) == time_format(b[i + 1][3]) and uniq_time <= 3:
        count += 1
    else:
        uniq_time += 1

if count > len(b):
    count = len(b)

maximum = [0, 0, 0, 0]
for i in range(0, count):
    for j in range(0, 4):
        if len(b[i][j]) > maximum[j]:
            maximum[j] = len(b[i][j])

for i in range(0, count):
    print("{:<{m1}} {:<{m2}} {:<{m3}} {:<{m4}}".format(b[i][0], b[i][1], b[i][2], b[i][3],
                                                       m1=maximum[0], m2=maximum[1], m3=maximum[2], m4=maximum[3]))

    print((Fraction("11")/Fraction("345") + (Fraction("5.56")+Fraction("32.30"))/Fraction("2.")) / Fraction("7"))

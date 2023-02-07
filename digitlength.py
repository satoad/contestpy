a = eval(input())

count1 = 1
i = 1
while count1 + (10 ** (i - 1) * 9) * i <= a:
    count1 += (10 ** (i - 1) * 9) * i
    i += 1

count2 = count1 + (10 ** (i - 1) * 9) * i
#print(count1, i - 1)
#print(count2, i)

L, R = 0, 10 ** (i - 1) - 1
#print(i, 'aobobobo')
#print(len(str(R)), R)

#print(i)
if a - count1 < count2 - a and a != count1:
    #R = 10 ** (i - 1) - 1
    if a - count1 < i:
        tmp = i - (a - count1)

        #print(tmp)
        if tmp <= 10:
            L += tmp
            R += 1
        else:
            L += 10
            tmp -= 10
            if (a - count1) % len(str(L)) == 0:
                L += int((len(str(R)) * (a - count1) - 10) / len(str(L)))
                R += a - count1
            else:
                L += int(tmp / len(str(L)))
                R += 1
    else:
        R = 10 ** (i - 1) - 1 + (a - count1) // i
        tmp = (a - count1) % i

        while tmp != 0:
            tmp += len(str(L))
            L += 1
            c = 0
            while tmp > 0:
                tmp -= i
                c += 1
                R += 1

elif a != count2 and a != count1:
    R = 10 ** (i - 1) - 1 + (a - count1) // i + 1
    tmp = (a - count1) % i

    while tmp != 0:
        tmp += len(str(L))
        L += 1
        if tmp > 0:
            tmp = tmp - i * (tmp // i)
            R += 1 * (tmp // i)


print(R - L + 1, L, R)


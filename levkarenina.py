def put_item(dict, item1):
    if item1 in dict.keys():
        dict[item1] += 1
    else:
        dict[item1] = 1

    return dict

def word_print(dict):
    word = ''
    max1 = 0

    if dict:
        for i in dict:
            if dict[i] > max1:
                word = i
                max1 = dict[i]
    else:
        word = '...'

    print(word, max1, end='')

p, b, g, e = input()

cond1 = {}
cond2 = {}

flag1 = False
while a := input():
    a = a.split()

    for i in a:
        if i[-1] == p and not flag1:
            flag1 = True
        elif i[0] == b and flag1:
            if i[-1] != p:
                flag1 = False

            put_item(cond1, i)
        elif flag1 and i[-1] != p:
            flag1 = False

        if i[-1] == e and i[0] == g:
            put_item(cond2, i)

word_print(cond1)
print(' - ', end='')
word_print(cond2)
print()
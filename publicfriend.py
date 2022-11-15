contacts = {}


while a := eval(input()):
    if a[0] != 0 or a[1] != 0:
        if a[0] in contacts.keys():
            contacts[a[0]].add(a[1])

            if a[1] in contacts.keys():
                contacts[a[1]].add(a[0])
            else:
                contacts[a[1]] = {a[0]}
        else:
            contacts[a[0]] = {a[1]}
            if a[1] in contacts.keys():
                contacts[a[1]].add(a[0])
            else:
                contacts[a[1]] = {a[0]}
    else:
        break


b = set()
for i in contacts.keys():
    if len(contacts[i]) == len(contacts.keys()) - 1:
        b.add(i)

b = sorted(b)
for i in range(0, len(b)):
    print(b[i], end=' ')
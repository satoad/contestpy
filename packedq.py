cort = tuple()

inp = eval(input())

for obj in inp:
    if type(obj) is int and obj <= len(cort):
        print(cort[:obj])
        
        if inp != 0:
            cort = cort[obj:]
    elif type(obj) is tuple:
        cort += obj
    else:
        break
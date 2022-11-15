def turtle(coord, direction):
    x, y = coord[0], coord[1]
    if direction == 1:
        flag = ['y', 1]
    elif direction == 2:
        flag = ['x', -1]
    elif direction == 3:
        flag = ['y', -1]
    elif direction == 0:
        flag = ['x', 1]

    while True:
        direct = yield x, y
        if direct == 'l':
            if flag[0] == 'x':
                flag[0] = 'y'
            else:
                if flag[1] == -1:
                    flag[1] = 1
                else:
                    flag[1] = -1
                flag[0] = 'x'

        if direct == 'r':
             if flag[0] == 'x':
                 flag[0] = 'y'
                 if flag[1] == -1:
                     flag[1] = 1
                 else:
                     flag[1] = -1
             else:
                 flag[0] = 'x'

        if direct == 'f':
            if flag[0] == 'x':
                x += flag[1] * 1
            else:
                y += flag[1] * 1

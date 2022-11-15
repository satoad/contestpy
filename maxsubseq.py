max_len = 0
cur_len = 0
b = 0

while (a := eval(input())) != 0:    
    if a >= b:
        cur_len += 1
    else:
        if (cur_len > max_len):
            max_len = cur_len
        cur_len = 0

    b = a

if cur_len + 1 > max_len:
    print(cur_len)
else:
    print(max_len + 1)

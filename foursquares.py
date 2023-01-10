n = eval(input())


#from datetime import datetime
#import time

#start_time = datetime.now()

for x in range(int((n**0.5) / 4), int(n**0.5) + 1):
    tmp_x = x**2
    for y in range(int(((n - tmp_x)**0.5) / 3), int((n - tmp_x)**0.5) + 1):
        if 0 <= y <= x:
            tmp_y = y**2
            for z in range(int(((n - tmp_x - tmp_y)**0.5) / 2), int((n - tmp_x - tmp_y)) + 1):
                tmp_z = z ** 2

                if not (tmp_x + tmp_y + tmp_z <= n):
                    break

                if 0 <= z <= y and 0 <= n - tmp_x - tmp_y - tmp_z <= tmp_z:
                    t = int((n - tmp_x - tmp_y - tmp_z)**0.5)
                    if tmp_x + tmp_y + tmp_z + t**2 == n:
                        print(x, y, z, t)

#print(datetime.now() - start_time)
n = eval(input())

for x in range(int((n**0.5) / 4), int(n**0.5) + 1):
    tmp_x = x**2
    for y in range(int(((n - tmp_x)**0.5) / 3), int((n - tmp_x)**0.5) + 1):
        if 0 <= y <= x:
            tmp_y = y**2
            for z in range(int(((n - tmp_x - tmp_y)**0.5) / 2), int((n - tmp_x - tmp_y)) + 1):
                if 0 <= z <= y and 0 <= n - tmp_x - tmp_y - z**2 <= z**2:
                    t = int((n - tmp_x - tmp_y - z**2)**0.5)
                    if tmp_x + tmp_y + z**2 + t**2 == n:
                        print(x, y, z, t)


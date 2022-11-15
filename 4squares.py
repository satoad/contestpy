n = eval(input())

for x in range (int((n**0.5) / 4), int(n**0.5) + 1):
    for y in range(int(((n - x**2)**0.5) / 3), int((n - x**2)**0.5) + 1):
        if 0 <= y <= x:
            for z in range(int(((n - x**2 - y**2)**0.5) / 2), int((n - x**2 - y**2)) + 1):
                if 0 <= z <= y and 0 <= n - x**2 - y**2 - z**2 <= z**2:
                    print(x, y, z)
                    t = int((n - x**2 - y**2 - z**2)**0.5)
                    if x**2 + y**2 + z**2 + t**2 == n:
                        print(x, y, z, t)  


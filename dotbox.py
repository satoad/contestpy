coords = [0, 0, 0, 0, 0, 0]

x, y, z = input()

while (x != ''):
    
    if x > coords[0]:
        coords[0] = x

    if x < coords[1]:
        coords[1] = x

    if y > coords[2]:
        coords[2] = y

    if y < coords[3]:
        coords[3] = y

    if z > coords[4]:
        coords[4] = z

    if z < coords[5]:
        coords[0] = z

print((coords[0] - coords[1]) * (coords[2] - coords[3]) * (coords[4] - coords[5]))        

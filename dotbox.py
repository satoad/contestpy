x = [None, None]
y = [None, None]
z = [None, None]
while a := input():
    tmp_x, tmp_y, tmp_z = a.split(',')
    tmp_x, tmp_y, tmp_z = float(tmp_x), float(tmp_y), float(tmp_z)

    if x[0] is None or tmp_x > x[0]:
        x[0] = tmp_x
    elif x[1] is None or tmp_x < x[1]:
        x[1] = tmp_x

    if y[0] is None or tmp_y > y[0]:
        y[0] = tmp_y
    elif y[1] is None or tmp_y < y[1]:
        y[1] = tmp_y

    if z[0] is None or tmp_z > z[0]:
        z[0] = tmp_z
    elif z[1] is None or tmp_z < z[1]:
        z[1] = tmp_z

if None in x or None in y or None in z:
    print(0.0)
else:
    print((x[0] - x[1]) * (y[0] - y[1]) * (z[0] - z[1]))
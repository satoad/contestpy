rectangles_info = []

min_x = min_y = float('inf')
max_x = max_y = float('-inf')

while rectangle := input():
    rectangle = rectangle.split()
    if int(rectangle[2]) and int(rectangle[3]):
        rectangles_info.append([int(rectangle[i]) for i in range(4)] + [rectangle[4]])
        min_x = min(min_x, rectangles_info[-1][0])
        max_x = max(max_x, rectangles_info[-1][0])
        min_y = min(min_y, rectangles_info[-1][1])
        max_y = max(max_y, rectangles_info[-1][1])

        if rectangles_info[-1][2] > 0:
            max_x = max(max_x, rectangles_info[-1][0] + rectangles_info[-1][2] - 1)
        else:
            min_x = min(min_x, rectangles_info[-1][0] + rectangles_info[-1][2])

        if rectangles_info[-1][3] > 0:
            max_y = max(max_y, rectangles_info[-1][1] + rectangles_info[-1][3] - 1)
        else:
            min_y = min(min_y, rectangles_info[-1][1] + rectangles_info[-1][3])


x_size = max_x - min_x + 1
y_size = max_y - min_y + 1
res = ['.' * x_size for _ in range(y_size)]


for rectangle in rectangles_info:
    x = rectangle[1] - min_y
    y = rectangle[0] - min_x
    left, right = min(y + rectangle[2], y), max(y + rectangle[2], y)
    up, down = min(x + rectangle[3], x), max(x + rectangle[3], x)
    for i in range(up, down):
        res[i] = res[i][:left] + rectangle[4] * abs(rectangle[2]) + res[i][right:]


for row in res:
    print(row)
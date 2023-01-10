from collections import Counter


class Spiral:
    def __init__(self, string):
        self.counter = Counter(string)

    def __str__(self):
        x, y = 0, 0
        left_lim = right_lim = upper_lim = lower_lim = 0
        direction = 0
        next_corner = 0
        part_len = 0
        field = {}

        for chars_placed, char in enumerate(self.counter.elements()):
            field[x, y] = char

            left_lim = min(left_lim, x)
            right_lim = max(right_lim, x)
            lower_lim = min(lower_lim, y)
            upper_lim = max(upper_lim, y)

            if chars_placed == next_corner:
                part_len += 1
                next_corner += part_len
                direction = (direction + 1) % 4

            x += (0, 1, 0, -1)[direction]
            y += (1, 0, -1, 0)[direction]

        right_lim += 1
        upper_lim += 1

        return '\n'.join(''.join(field.get((x, y), ' ') for x in range(left_lim, right_lim))
                         for y in range(lower_lim, upper_lim))

    def __add__(self, other):
        return Spiral(list(self) + list(other))

    def __sub__(self, other):
        return Spiral(self.counter - other.counter)

    def __mul__(self, times):
        return Spiral(times * list(self))

    __rmul__ = __mul__

    def __iter__(self):
        return self.counter.elements()

    def __len__(self):
        return sum(self.counter.values())


class Spiral:
    def __init__(self, other):
        self.symbs = other
        count = len(other)

        i = 0
        while count - i > 0:
            count -= i
            i += 1

        self.symbs += " " * (i - count - 1)

        self.turn = i
        self.w = i
        self.h = i

        if count != 0:
            if i % 2 == 0:
                self.h -= 1
            else:
                self.w -= 1

    def __add__(self, other):
        tmp = self.symbs.split()
        return Spiral(tmp[0] + other.symbs)

    def __sub__(self, other):
        new_obj = Spiral(self.symbs)
        for x in other.symbs:
            new_obj.symbs.replace(x, '', 1)
        return new_obj

    def __mul__(self, other):
        return type(self)(self.symbs * other)

    __rmul__ = __mul__

    def __iter__(self):
        for i in self.symbs:
            yield i

    def __repr__(self):
        screen = [[" "] * self.w for i in range(self.h)]

        vect = self.turn % 4
        i = len(self.symbs) - 1

        turns = self.turn

        pos_h = 0
        pos_w = 0

        flag = True

        if vect == 3:
            pos_h = 0
            pos_w = 0
        elif vect == 2:
            pos_h = 0
            pos_w = self.w - 1
        elif vect == 1:
            pos_h = self.h - 1
            pos_w = self.w - 1
        elif vect == 0:
            pos_h = self.h - 1
            pos_w = 0

        while turns > 0:
            if vect == 3:
                lim = self.turn
                if not flag:
                    pos_h += 1
                    pos_w += 1
                else:
                    if self.h > self.w:
                        lim -= 1
                flag = False

                j = self.turn - turns
                while i >= 0 and j < lim:
                    screen[pos_h][pos_w] = self.symbs[i]
                    i -= 1
                    pos_w += 1
                    j += 1

            elif vect == 2:
                lim = self.turn
                if not flag:
                    pos_w -= 1
                    pos_h += 1
                else:
                    if self.h < self.w:
                        lim -= 1
                flag = False
                j = self.turn - turns

                while i >= 0 and j < lim:
                    p = screen[pos_h][pos_w]
                    screen[pos_h][pos_w] = self.symbs[i]
                    i -= 1
                    pos_h += 1
                    j += 1

            elif vect == 1:
                lim = self.turn
                if not flag:
                    pos_w -= 1
                    pos_h -= 1
                else:
                    if self.h > self.w:
                        lim -= 1
                flag = False

                j = self.turn - turns
                while i >= 0 and j < lim:
                    screen[pos_h][pos_w] = self.symbs[i]
                    i -= 1
                    pos_w -= 1
                    j += 1
            elif vect == 0:
                lim = self.turn
                if not flag:
                    pos_w += 1
                    pos_h -= 1
                else:
                    if self.h < self.w:
                        lim -= 1
                flag = False

                j = self.turn - turns
                while i >= 0 and j < lim:
                    screen[pos_h][pos_w] = self.symbs[i]
                    i -= 1
                    pos_h -= 1
                    j += 1

            turns -= 1
            vect = turns % 4

        tmp = ''
        for l in screen:
            tmp += "".join(l) + '\n'

        tmp = tmp[:-1]
        return tmp
class Pushpull:
    pos = [0]

    def pull(self, step=1):
        self.pos[0] -= step

    def push(self, step=1):
        self.pos[0] += step

    def __init__(self, num=0):
        self.pos[-1] = num

    def __repr__(self):
        if self.pos[0] > 0:
            return f">{self.pos[0]}>"
        elif self.pos[0] < 0:
            return f"<{abs(self.pos[0])}<"
        else:
            return "<0>"

    def __iter__(self):
        if self.pos[0] > 0:
            return iter(list(i for i in range(0, self.pos[0])))
        else:
            return iter(list(i for i in range(0, self.pos[0], -1)))

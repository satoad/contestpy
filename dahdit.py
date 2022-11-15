class morse:
    inp_morse = ''

    def __init__(self, other="di dit dah"):
        self.symbs = {}
        self.flag = False

        tmp = other

        if ' ' in other:
            self.flag = True
            other = other.split()

        for i in range(0, len(other)):
            self.symbs[i] = other[i]

        if len(other) == 2:
            self.symbs[2] = self.symbs[1]
            self.symbs[1] = other[0]

        if tmp[-1] == ' ':
            self.symbs[3] = ' '

    def __repr__(self):
        i = 0

        text = ''
        while i < len(self.inp_morse):
            if self.inp_morse[i] == '-':
                text += self.symbs[2]

                if i + 1 < len(self.inp_morse) and self.inp_morse[i + 1] != '~' and self.flag:
                    text += ' '

            elif self.inp_morse[i] == '+' and i + 1 < len(self.inp_morse) and self.inp_morse[i + 1] == '~':
                text += self.symbs[1]

            elif self.inp_morse[i] == '~':
                if self.flag:
                    text += ','
                text += ' '

            elif self.inp_morse[i] == '+' and i + 1 == len(self.inp_morse):
                text += self.symbs[1]
                break

            elif self.inp_morse[i] == '+':
                text += self.symbs[0]
                if self.flag:
                    text += ' '

            i += 1

        if 3 in self.symbs.keys():
            text += self.symbs[3]

        elif self.flag:
            text += '.'

        return text

    def __neg__(self):
        self.inp_morse = '-' + self.inp_morse
        return self

    def __pos__(self):
        self.inp_morse = '+' + self.inp_morse
        return self

    def __invert__(self):
        self.inp_morse = '~' + self.inp_morse
        return self

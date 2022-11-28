import sys


def decode(text, code, samples, num):
    if num == 3:
        return None

    if text is not None:
        for i in samples[code]:
            tmp = text.encode(code).decode(i[0])
            print(tmp)
            if tmp.split(' ')[0] == i[1]:
                return tmp
            else:
                if i[0] in samples.keys():
                    return decode(tmp, i[0], samples, num + 1)
                else:
                    return None


ciphers = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258',
               'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874',
               'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1',
               'mac_croatian',  'mac_greek', 'mac_iceland', 'mac_latin2']

example = 'ПРОЦ'

samples = {}

for i in ciphers:
    for j in ciphers:
        try:
            tmp = example.encode(i).decode(j)
            if i in samples.keys():
                samples[i].append([j, tmp])
            else:
                samples[i] = [[j, tmp]]
        except UnicodeEncodeError:
            continue
        except UnicodeDecodeError:
            continue

a = sys.stdin.read()

for i in samples:
    print(i, " ", samples[i])

res = ''
for i in samples:
    res = decode(a, i, samples, 0)
    print(res)
    if res is not None:
        break

print(res)
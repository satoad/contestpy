import sys

encodings = [
    'cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256',
    'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855',
    'cp864', 'cp866', 'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16',
    'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2'
]

encoding_pairs = [(e1, e2) for e1 in encodings for e2 in encodings if e1 != e2]

alphabet = '!\"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ'.encode('koi8_r')
samples = ['ПРОЦ', 'КНЦ;']

inp = sys.stdin.read().strip()

_el1 = None

if inp[:4] == samples[0] and inp[-4:] == samples[1]:
    print(inp)
    sys.exit(0)

pairs = {}

find_flag = False

for el1, el2 in encoding_pairs:
    try:
        encoded = alphabet.decode(el1).encode(el2)
    except Exception:
        continue

    pairs[((el2, el1),)] = encoded

    try:
        first_word = inp[:4].encode(el1).decode('koi8-r')
        second_word = inp[-4:].encode(el1).decode('koi8-r')
    except Exception:
        continue

    if samples[0] == first_word and samples[1] == second_word:
        _el1 = el1
        find_flag = True
        break

if find_flag:
    print(inp.encode(_el1).decode('koi8_r'))
else:
    new_pairs = {}

    for i, j in pairs.items():
        for el1, el2 in encoding_pairs:
            if i[0][0] == el1:
                continue

            try:
                j.decode(el1).encode(el2)
            except Exception:
                continue

            cods = ((el2, el1),) + i
            new_pairs[cods] = j.decode(el1).encode(el2)

            ((c1, c2), (c3, c4)) = cods

            try:
                first_word = inp[:4].encode(c2).decode(c3).encode(c4).decode("koi8_r")
                second_word = inp[-4:].encode(c2).decode(c3).encode(c4).decode("koi8_r")
            except Exception:
                continue

            if samples[0] == first_word and samples[1] == second_word:
                print(inp.encode(c2).decode(c3).encode(c4).decode("koi8_r"))
                break
    else:
        for i, j in new_pairs.items():
            for el1, el2 in encoding_pairs:
                if i[0][0] == el1:
                    continue

                try:
                    j.decode(el1).encode(el2)
                except Exception:
                    continue

                cods = ((el2, el1),) + i

                ((c1, c2), (c3, c4), (c5, c6)) = cods

                try:
                    first_word = inp[:4].encode(c2).decode(c3).encode(c4).decode(c5).encode(c6).decode("koi8_r")
                    second_word = inp[-4:].encode(c2).decode(c3).encode(c4).decode(c5).encode(c6).decode("koi8_r")
                except Exception:
                    continue

                if samples[0] == first_word and samples[1] == second_word:
                    print(inp.encode(c2).decode(c3).encode(c4).decode(c5).encode(c6).decode("koi8_r"))
                    sys.exit(0)
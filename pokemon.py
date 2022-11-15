def put_deck(dict, item1, item2):
    if item1 in dict.keys():
        dict[item1].add(item2)
    else:
        dict[item1] = {item2}

    return dict


players = {}
deck = {}

while a := input():
    a = a.split('/')
    if a[0][0].isdigit():
        deck = put_deck(deck, a[0][:len(a[0]) - 1], a[1][1:])
    else:
        players = put_deck(players, a[0], a[1][1:])

maximum = 0
for i in players.keys():
    tmp = 0
    tmp_set = set()
    for j in players[i]:
        tmp_set |= deck[j]

    tmp = len(tmp_set)
    if tmp > maximum:
        maximum = tmp

    players[i] = tmp

b = set()
for i in players:
    if players[i] == maximum:
        b.add(i)

b = sorted(b)
for i in range(0, len(b)):
    print(b[i])
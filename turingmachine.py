LIMIT = 100000

alphabet = []
alp_flag = False
rules = {}
word = ''

while inp := input():
    if not alp_flag:
        alp_flag = True
        alphabet = inp.split()
    else:
        if not ' ' in inp:
            word = inp
            break

        inp = inp.split()
        rules[inp[0]] = {}
        for j in range(len(alphabet)):
            rules[inp[0]][alphabet[j]] = inp[j + 1].split(',')


count = 0
cur = [0, 0]
while count != LIMIT:
    task = rules[str(cur[0])][word[cur[1]]]

    if task[0] != '':
        word = word[:cur[1]] + task[0] + word[cur[1] + 1:]

    match task[1]:
        case 'L':
            cur[1] -= 1
        case 'R':
            cur[1] += 1

    if cur[1] >= len(word):
        word += '_'
    elif cur[1] < 0:
        word = '_' + word
        cur[1] += 1

    if task[2] != '':
        if task[2] == '!':
            break
        cur[0] = int(task[2])

    count += 1

if count != LIMIT:
    print(word.replace('_', ''))


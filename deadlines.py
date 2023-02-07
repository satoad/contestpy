from bisect import bisect

deadlines, total_penalty, days = [], 0, [i for i in range(200000)]
while s := input():
    deadlines.append(((pair := list(map(int, s.split())))[1], pair[0]))
for penalty, day in sorted(deadlines, reverse=True):
    if bis := bisect(days, day):
        tmp = days[bis - 1]
        del days[bis - 1]
    if not tmp:
        total_penalty += penalty
print(total_penalty)


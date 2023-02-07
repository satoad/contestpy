words = []
while inp := input():
    words.append(inp)

words = sorted(words)

k = len(words[0])
for i in range(1, len(words), 2):
    while words[i - 1][:k] != words[i][:k]:
        k -= 1

print(k)


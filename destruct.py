import base64


def hex_to_sint(hexstr, bits):
     value = int(hexstr, 16)
     if value & (1 << (bits-1)):
         value -= 1 << bits

     return value

inp = input()
inp = str.encode(inp)
a = base64.b85decode(inp).hex()
inp = base64.b85decode(inp)

b = [a[i:i+2] for i in range(0, len(a), 2)]
c = b[:b.index('00')]

head = []
for i in c:
    head.append(hex_to_sint(i, 8))

prev = inp.index(b'\x00') + 1
res = 0
i = 0

while prev < len(inp):
    cur = head[i % len(head)]

    if cur > 0:
       # print(inp[prev:prev + cur], ' ', inp[prev:prev + cur].hex())
        res += int.from_bytes(inp[prev:prev + cur], byteorder='big', signed=False)
    else:
       # print(inp[prev:prev + abs(cur)], ' ', inp[prev:prev + abs(cur)].hex())
        res += int.from_bytes(inp[prev:prev + abs(cur)], byteorder='big', signed=True)

    prev += abs(cur)
    i += 1

print(res)
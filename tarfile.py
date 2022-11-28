import tarfile
import sys
import io

a = sys.stdin.read().strip().replace('\n', '')
f = io.BytesIO(bytes.fromhex(a))


res = [0, 0]

with tarfile.open(fileobj=f, mode='r') as tar:
    for file in tar.getmembers():
        if file.isfile():
            res[0] += file.size
            res[1] += 1

print(*res)
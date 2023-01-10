import os


test_file = open('./tmp.py', 'w')

while string := input():
    if len(string) >= 8 and string[:5] == 'class':
        test_file.write(string[:string.find(':')] + ': pass\n')

test_file.close()

try:
    import tmp
except Exception:
    print('No')
else:
    print('Yes')

os.remove('./tmp.py')
import sys
count = 0
for i in range(8):
    l = sys.stdin.readline()
    if i%2 == 0:
        l = l[::2]
    else:
        l = l[1::2]
    n = l.count('F')
    count += n

print(count)
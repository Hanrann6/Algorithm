import sys
n = int(sys.stdin.readline())
f = int(sys.stdin.readline())

min = (n // 100) * 100

k = min // f
if (min % f) == 0:
    count = min
else:
    count = f * k + f
print(str(count)[-2:])

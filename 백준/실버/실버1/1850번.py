import sys
input = sys.stdin.readline

a, b = map(int, input().split())
mo = b % a
while mo != 0:
    b, a = a, mo
    mo = b % a
for _ in range(a):
    print(1, end='')
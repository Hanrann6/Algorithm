import sys
input = sys.stdin.readline

ns = input().strip()
while int(ns) != 0:
    if int(ns) == int(ns[::-1]):
        print('yes')
    else:
        print('no')
    ns = input()
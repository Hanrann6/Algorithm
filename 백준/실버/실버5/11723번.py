import sys
input = sys.stdin.readline

all_list = [i for i in range(1, 21)]
n = int(input())
s = set()
# 1  3
for _ in range(n):
    method = input().rstrip()
    if method[:3] == 'add':
        m0, m1 = method.split()
        m1 = int(m1)
        s.add(m1)
    elif method[:5] == 'check':
        m0, m1 = method.split()
        m1 = int(m1)
        if m1 in s:
            print(1)
        else:
            print(0)
    elif method[:6] == 'remove':
        m0, m1 = method.split()
        m1 = int(m1)
        if m1 in s:
            s.remove(m1)
    elif method[:6] == 'toggle':
        m0, m1 = method.split()
        m1 = int(m1)
        if m1 in s:
            s.remove(m1)
        else:
            s.add(m1)
    elif method == "empty":
        s.clear()
    elif method == "all":
        s = set(all_list)
import sys
input = sys.stdin.readline

stk = [] # 스택
n = int(input())

for _ in range(n):
    s = input().strip() + "   " # 최소 크기 6
    if s[:4] == 'push':
        push, n = s.split()
        stk.append(n)
    elif s[:3] == 'pop':
        if not stk:
            print(-1)
        else:
            print(stk.pop())
    elif s[:4] == 'size':
        print(len(stk))
    elif s[:5] == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    elif s[:3] == 'top':
        if not stk:
            print(-1)
        else:
            print(stk[-1])

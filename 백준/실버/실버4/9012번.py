import sys
input = sys.stdin.readline

n = int(input())

def isPs(ps):
    # 스택 사용
    stk = []
    for s in ps:
        if len(stk) == 0:
            stk.append(s)
        elif (stk[-1] == '(') and (s == ')'):
            stk.pop()
        else:
            stk.append(s)
    if len(stk) == 0:
        return True
    else:
        return False


for _ in range(n):
    ps = input().strip() # 괄호 문자열
    if isPs(ps):
        print('YES')
    else:
        print('NO')
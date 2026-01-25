import sys
input = sys.stdin.readline

s = input().rstrip()
while(s != '.'):
    stack = []
    p = 'yes'
    for c in s: # 한글자씩 확인
        if(c == '(' or c == '['):
            stack.append(c)
        elif(c == ')'):
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                p = 'no'
                break
        elif(c == ']'):
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                p = 'no'
                break
        else:
            continue
    if len(stack) != 0:
        p = 'no'
    print(p)
    s = input().rstrip()



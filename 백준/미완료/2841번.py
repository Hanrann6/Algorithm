import sys
input = sys.stdin.readline
n, p = map(int, input().split())
#스택
count=0

num = [[] for _ in range(6)] #줄별로 하나
for i in range(n):
    a, b = map(int, input().split())
    num[a].append(b)

for i in range(6):
    if not num[i]:
        continue
    stack = []
    for k in num[i]:
        if not stack:
            stack.append(k)
            count += 1
        elif(k > stack[-1]):
            stack.append(k)
            count += 1
        elif(k == stack[-1]):
            continue
        else:
            while k < stack[-1]:
                stack.pop()
                count += 1
                if not stack:
                    break
            if not stack:
                stack.append(k)
                count += 1
            if(k==stack[-1] or not stack):
                continue
            else:
                stack.append(k)
                count += 1
print(count)
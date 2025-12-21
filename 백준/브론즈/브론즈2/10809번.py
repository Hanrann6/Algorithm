import string
import sys
input = sys.stdin.readline

s = input()
ans = []
# 알파벳 26개. a-z 함수!! 신기
alpha = string.ascii_lowercase
for a in alpha:
    if a in s:
        ans.append(s.index(a))
    else:
        ans.append(-1)

print(*ans)
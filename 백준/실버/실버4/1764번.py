import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = {input().strip() for _ in range(n)}
b = {input().strip() for _ in range(m)}

ab = a & b # 교집합
print(len(ab))
ab = list(ab)
ab.sort()
for i in ab:
    print(i)

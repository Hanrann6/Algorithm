import sys
input = sys.stdin.readline

n = int(input()) # 참가자 수
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠
totT = 0
for s in sizes:
    if s % T == 0:
        totT += s // T
    else:
        totT += s // T + 1

print(totT)

# 펜
print(n//P, n%P)
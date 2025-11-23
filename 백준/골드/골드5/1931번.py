import sys
input = sys.stdin.readline
n = int(input())
conf = []
for _ in range(n):
    li = list(map(int, input().split()))
    conf.append(li)

conf.sort(key=lambda x: (x[1], x[0])) #끝나는 시간 기준으로

cnt=0
end = -1
for i in range(n):
    a, b = conf[i]
    if a >= end:
        end = b
        cnt += 1

print(cnt)
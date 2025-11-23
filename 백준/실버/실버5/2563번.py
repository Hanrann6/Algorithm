import sys
input = sys.stdin.readline

sq = [[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for k in range(10):
            sq[x+i][y+k] = 1

total=0
for i in range(100):
    total += sum(sq[i])
print(total)
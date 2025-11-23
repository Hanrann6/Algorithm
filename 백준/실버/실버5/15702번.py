import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #문제 수, 응시자수
score = list(map(int, input().split()))
std = [[0, 0] for _ in range(m)]  #번호, 점수 배열

for i in range(m):
    s = list(input().split())
    num, ox = int(s[0]), s[1:] #입력 받기
    std[i][0] = num
    for j in range(n):
        if(ox[j] == 'O'):
            std[i][1] += score[j]

ans = max(std, key = lambda x:(x[1], -(x[0])))
print(*ans)
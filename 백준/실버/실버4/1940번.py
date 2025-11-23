import sys
input = sys.stdin.readline
n = int(input()) #재료의 개수
m = int(input()) #갑옷수
num = list(map(int, input().split())) #재료 고유번호
count=0
for _ in range(n):
    p = num.pop()
    if(p == m or p == 0):
        continue
    min = m - p
    if(min in num): #짝이 있으면 count += 1
        count += 1
        for k in num:
            if(k == min):
                num.remove(k) #짝도 없애줌
    if(len(num)==0):
        break
print(count)

# 실버 4, 성공
#첨엔 리스트 =0으로 했는데 시간초과.
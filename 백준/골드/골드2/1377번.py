import sys
input = sys.stdin.readline
n = int(input())
start_i = dict() #시작 인덱스
end_i = dict() #정렬 후 인덱스
num=[]
d=[]
for i in range(n): #시작 인덱스 저장
    k = int(input())
    start_i[k] = i
    num.append(k)
num.sort()

for i in range(n): #정렬 후 인덱스 저장
    end_i[num[i]] = i

# 왼쪽으로 가장 많이 이동한 횟수가 정렬 횟수! +1
for i in range(n):
    d.append(start_i[num[i]] - end_i[num[i]])
ans = max(d) + 1 #한 번은 false가 나와야 하니까
print(ans)
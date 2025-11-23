import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

#자기 자신을 제외한 두 수의 합!!
#마이너스도 가능..!! -> 투포인터 사용
num.sort()
count=0
for i in range(n):
    start, fin = 0, n-1 #투포인터 선언.
    while start < fin:
        if(start==i):
            start += 1
            continue
        if(fin==i):
            fin -= 1
            continue
        total = num[start]+num[fin]
        if(total==num[i]):
            count += 1
            break
        elif(total > num[i]):
            fin -= 1
        else:
            start += 1

print(count)
'''
골드 4, 도움을 많이 받아 성공
sum = set()
for i in range(n-1):
    for k in range(i+1, n):
        sum.add(num[i] + num[k])
count=0
for i in num:
    if(i in sum):
        count += 1
print(count)

sum = {}
for i in range(n-1):
    for k in range(i+1, n):
        if((num[i] + num[k]) in sum):
            sum[num[i] + num[k]] += 1
        sum[num[i] + num[k]] = 1
count =0
for i in num:
    if(i in sum):
        count += sum[i]
print(count)
'''

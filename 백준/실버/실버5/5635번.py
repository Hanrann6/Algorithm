#5635번
from datetime import datetime #날짜 모듈
n = int(input())
name = []
date = []

for i in range(n):
    n, dd, mm, yyyy = input().split()
    name.append(n)
    date.append(datetime(int(yyyy), int(mm), int(dd)))

print(name[date.index(max(date))])
print(name[date.index(min(date))])

#birth = [[] for _ in range(n)] #n행 배열 선언
#birth[i] = [name, dd, mm, yyyy] #i행에 이름, 일, 월, 년 추가
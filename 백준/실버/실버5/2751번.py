import sys
input = sys.stdin.readline
n = int(input())
num = [int(input().strip()) for _ in range(n)]
#근데 sort()보다 시간 3배 걸림...
#합병 나누기
def merge_sort(num):
    if(len(num)<=1):
        return num
    mid = len(num)//2
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])
    return merge(left, right)
#합병
def merge(left, right):
    i, j = 0, 0
    nlist = []
    while(i < len(left)) and (j < len(right)):
        if(left[i] < right[j]):
            nlist.append(left[i])
            i += 1
        else:
            nlist.append(right[j])
            j += 1
    nlist.extend(left[i:])
    nlist.extend(right[j:])
    return nlist

mnum = merge_sort(num)
for i in range(n):
    print(mnum[i])
'''
#2751번 - 실버 5
#시간초과 -> 해결
import sys

n = int(input())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline())) #정수를 입력받는데서 시간초과였다. sort가 문제가 아녔다. input()를 sys 모듈로 입력받는 것으로 바꿔줌

list.sort()
for i in list:
    print(i)


# O(n)이 커서 힙 정렬으로
# 이것도 시간 초과임..
import heapq

n = int(input())
list = []
for _ in range(n):
    i = int(input())
    list.append(i) # 여기까진 위와 동일

heapq.heapify(list)
nlist=[]

while list:
    nlist.append(heapq.heappop(list))

for i in nlist:
    print(i)
'''
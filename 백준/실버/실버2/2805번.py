import sys
input = sys.stdin.readline

#나무의 수, 필요한 m
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    sum=0
    for i in tree:
        if i > mid:
            sum += (i - mid)
    if(sum < m): #나무 부족함
        end = mid - 1
    else: #나무 넘쳐남
        start = mid + 1

print(end) #높이의 최댓값을 구하는 것이라서
#python은 시간초관데 pypy3으로 하니깐 됨..
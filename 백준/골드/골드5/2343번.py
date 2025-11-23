import sys
input = sys.stdin.readline
n, key = map(int, input().split())
mlist = list(map(int, input().split()))

start = max(mlist)
end = sum(mlist)
ans = end
while start <= end:
    mid = (start + end) // 2
    count = 1 #블루레이 개수. 1번 나누면 2개 되니까 기본이 1개
    time = 0 #블루레이의 강의 길이
    for i in mlist:
        if(time + i) > mid:
            count += 1 #블루레이 1개 추가하고 다음 블루레이로 넘어감
            time = 0
        time += i
    if(count > key):
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)

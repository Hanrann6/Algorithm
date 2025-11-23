import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 점 개수, 선 개수
dot = list(map(int, input().split())) # 점
line = [list(map(int, input().split())) for _ in range(m)]
dot.sort()

# 이분탐색
def start_dot(a): # 가장 초기 점 인덱스
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if dot[mid] < a: # 시작점보다 작으면
            start = mid + 1
        else: # 시작점보다 크면
            end = mid - 1
    return start

'''
중요!
끝점을 찾을 때 답의 후보가 mid = b에 있기 때문에
끝점에는 <=b에 등호를 붙여야 함!
반대로 시작점 a의 경우엔
시작점보다 큰 경우 else에 등호가 포함된 것
'''
def end_dot(b): # 가장 끝 점 인덱스
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if dot[mid] <= b:  # 끝보다 작으면
            start = mid + 1
        else:  # 시작점보다 크면
            end = mid - 1
    return end


for l in line:
    a, b = l # 시작점, 끝점
    start_i = start_dot(a)
    end_i = end_dot(b)
    print(end_i - start_i + 1)



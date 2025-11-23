import sys
input = sys.stdin.readline

# 개쩌는 중복 개수 구하는 방법 - set & 사용
# import sys
# input = sys.stdin.readline
#
# while True:
#     a, b = map(int, input().split())  # 상근, 선영
#     if a == 0 and b == 0:
#         break
#     a_list = {int(input()) for _ in range(a)}
#     b_list = {int(input()) for _ in range(b)}
#     print(len(a_list&b_list))

while True:
    a, b = map(int, input().split())  # 상근, 선영
    if a == 0 and b == 0:
        break
    a_list = [int(input()) for _ in range(a)]
    b_list = [int(input()) for _ in range(b)]


    # 이분탐색
    def search(target, l):
        start, end = 0, len(l) - 1
        while start <= end:
            mid = (start + end) // 2
            if l[mid] > target:
                end = mid - 1
            elif l[mid] == target:
                return True
            else:
                start = mid + 1
        return False


    cnt = 0
    if a < b:  # a가 더 적으면, b에서 탐색
        for aa in a_list:
            if search(aa, b_list):
                cnt += 1
    else:
        for bb in b_list:
            if search(bb, a_list):
                cnt += 1

    print(cnt)


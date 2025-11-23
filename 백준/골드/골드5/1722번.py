import sys
import math
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
if num_list[0] == 1: # 케이스 1 - k번째 순열
    k = num_list[1] - 1
    numbers = list(range(1, n + 1))

    result = []

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1) # 남은 자리수에 대한 순열 수
        index = k // fact
        result.append(numbers.pop(index)) # 해당 숫자 선택
        k %= fact # 다음 자리수 진행

    print(" ".join(map(str, result)))
else:
    numbers = list(range(1, n + 1))
    order = 1
    arr = num_list[1:]

    for i in range(n):
        index = numbers.index(arr[i]) # 현재 숫자 인덱스
        order += index * math.factorial(n - 1 - i) # 인덱스만큼 경우의 수 누적
        numbers.pop(index) # 사용한 숫자 제거

    print(order)

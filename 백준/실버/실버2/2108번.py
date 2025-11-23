#2108번
import sys
import statistics
from collections import Counter
n = int(sys.stdin.readline()) # n개
num = [] # 숫자 리스트
sum = 0

for _ in range(n):
    a = int(sys.stdin.readline())
    sum += a
    num.append(a)

print(round(sum/n)) #산술평균
print(statistics.median(num)) #중앙값


counter = Counter(num)
most_common = counter.most_common()  # 가장 빈도가 높은 값

most_common_values = [x[0] for x in most_common if x[1] == most_common[0][1]]

if len(most_common_values) > 1:
    most_common_values.sort()
    print(most_common_values[1])
else:
    print(most_common_values[0])

print(max(num) - min(num)) #범위
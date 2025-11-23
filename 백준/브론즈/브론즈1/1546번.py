import sys
import statistics
n = int(sys.stdin.readline()) # 과목 개수
sc_list = list(map(int, sys.stdin.readline().split())) # 과목 별 점수
max = max(sc_list) # 최고점
new_list = list(map(lambda x: x/max*100, sc_list)) # 각 요소에 대해 새로운 함수 적용
print(statistics.mean(new_list))
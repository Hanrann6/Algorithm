import sys
n = int(sys.stdin.readline()) #학생수
li = list(sys.stdin.readline().split()) #학생 리스트
dic = {}
for i in range(n):
    dic[li[i]] = 0


for _ in range(n):
    love = list(sys.stdin.readline().split())
    for i in love:
        dic[i] += 1

# dict를 value를 기준으로 정렬하기, 내림차순
sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

#dict의 key, value 요소를 순서대로 출력하기
for key, value in sorted_dic.items():
    print(key, value)
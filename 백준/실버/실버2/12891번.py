import sys
input = sys.stdin.readline
s, p = map(int, input().split())
#s는 문자열 길이, p는 부분문자열의 길이
str = input()
a, c, g, t = map(int, input().split())
ans=0
count = {'A': 0, 'C':0, 'G':0, 'T':0}
# count()함수 시간 많이 잡아먹음 -> 슬라이딩 윈도우를 통해 범위 내 재사용!

#첫 번째 문자열 등록
for i in range(p):
    count[str[i]] += 1

if(count['A']>=a and count['C']>=c and count['G']>=g and count['T']>=t):
    ans += 1

for i in range(s-p):
    count[str[i]] -= 1
    count[str[i+p]] += 1
    if (count['A'] >= a and count['C'] >= c and count['G'] >= g and count['T'] >= t):
        ans += 1

print(ans)
'''
실버 2, 성공
9 4
GATTCGATC
'''
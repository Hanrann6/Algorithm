import sys
input = sys.stdin.readline

s = input().strip()
sub = set() # 부분 문자열
for i in range(1, len(s)+1): # 슬라이싱 길이
    for j in range(0, len(s)-i+1):
        wind = s[j:i+j]
        sub.add(str(wind))  # 추가

print(len(sub))
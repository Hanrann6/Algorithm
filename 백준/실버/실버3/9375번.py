import sys
input = sys.stdin.readline

def wear(cloth):
    ans = 1
    for cnt in cloth.values():
        ans *= (cnt+1)
    ans -= 1
    return ans


t = int(input()) # tk 수
for _ in range(t):
    n = int(input()) # 의상 수
    cloth = {} # 옷장
    # 데이터 저장
    for _ in range(n):
        name, c = input().strip().split() # 이름, 타입
        if c not in cloth.keys():
            cloth[c] = 1
        else: # 이미 종류가 있으면
            cloth[c] += 1
    print(wear(cloth))

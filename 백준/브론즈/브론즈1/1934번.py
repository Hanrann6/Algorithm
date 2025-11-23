# 최소 공약수는 유클리드 호제법 mod 연산으로 구함
# 최대 공배수는 A*B/최대공약수 로 계산
import sys
input = sys.stdin.readline
t = int(input()) #테스트케이스 수
for _ in range(t):
    a, b = map(int, input().split())
    mx = a * b
    mo = b % a
    while mo != 0:
        b, a = a, mo
        mo = b % a
    print(int(mx / a))


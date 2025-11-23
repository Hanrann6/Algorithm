import sys
input = sys.stdin.readline
n = int(input())
b=0
ans=1
for _ in range(n//2): #약수 구하기
    b += 1
    a = 2 * b + 1
    if(n % a == 0): #약수가 홀수면 ans += 1
        ans += 1

print(ans)
'''
실버 5, 성공
2 = 2
3 = 3, 1+2
4 = 4
5 = 5, 2+3
6 = 6, 1+2+3
7 = 7, 3+4
8 = 8
9 = 9, 2+3+4, 4+5
10 = 10, 1+2+3+4

1+2+3+4+5+6+7...
n의 3배수, 5배수, 7배수...(n>=2)
약수 중 홀수의 개수
'''

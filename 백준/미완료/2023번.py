import sys
sys.setrecursionlimit(10000)
import math

n = int(input())
prime_list = [] #소수 저장 배열. 각 자리별로

def prime(): #소수 검사
    number = int(''.join(map(str, prime_list))) #1개의 숫자로
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def recursive():
    if len(prime_list) == n:
        print(''.join(map(str, prime_list)))
        return
    for i in range(1, 10):
        prime_list.append(i)
        if prime(): #소수 맞으면 반복
            recursive()
        prime_list.pop()

recursive()
#블로그 보고함
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
def is_sosu(num):
    for i in range(2, int(num//2 + 1)):
        if num % i ==0:
            return False
    return True

def dfs(k):
    if len(str(k))==n:
        print(k)
    else:
        for i in range(1, 10):
            if i % 2 ==0:
                continue
            if is_sosu(k*10 + i):
                dfs(k*10 + i)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
#책보고함
'''
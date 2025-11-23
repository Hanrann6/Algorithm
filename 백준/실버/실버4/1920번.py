import sys
sys.setrecursionlimit(500)
input = sys.stdin.readline

#이진탐색
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split())) #M들의 집합

A.sort() #정렬

def binary(a, start, end, b): #이진탐색함수
    if start > end:
        return -1
    mid = (start + end) // 2 #가운데 인덱스
    if(b == a[mid]):
        return mid
    elif(b < a[mid]):
        end = mid - 1
    else:
        start = mid + 1
    return binary(a, start, end, b)

for i in B:
    ans = binary(A, 0, n-1, i)
    if ans >= 0:
        print(1)
    else:
        print(0)




'''
#그냥 탐색
#1920번 - 실버 4
import sys
n = int(input())
num1 = set(sys.stdin.readline().split())
#변수명으로 list를 사용하면 이후에 list 생성시 typeError문제됨
#list보다 set이 시간 복잡도가 더 낮다

m = int(input())
num2 = list(sys.stdin.readline().split())

for i in num2:
    if i in num1: #if 문에서 in을 사용해 포함돼있는지 확인 가능
        print(1)
    else:
        print(0)
'''
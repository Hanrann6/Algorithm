import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
print(num[k-1])

'''
시간초과??
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, input().split()))

#퀵 정렬
def quick(num):
    if(len(num)<=1): #빈 리스트도 가능해서 ==1은 안 됨
        return num
    pi = num[0]
    left = [x for x in num[1:] if x <= pi]
    right = [x for x in num[1:] if x > pi]
    return quick(left) + [pi] + quick(right) #리스트 결합이라 pi도 [pi]로!

num = quick(num)
print(num[k-1])
'''
import sys # 성공
n = int(input()) #테스트 개수
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    if a==0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        if b %2 == 1:
            print(a)
        else:
            print(a*a%10)
    else:
        b %= 4
        if b == 0: #b가 0이 되는 경우도 생각해야 됨
            print(a**4%10)
        else:
            print(a**b%10)

'''
1이면 1
2이면 2, 4, 8, 6
3이면 3, 9, 7, 1
4이면 4, 6
7먄 7, 9, 3, 1
8면 8, 4, 2, 6
9면 9, 1
'''
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
while a != 0:
    # c가 가장 길 때
    if (a**2 + b**2 == c**2):
        print("right")
    # c가 가장 길지 않을 때
    elif (abs(a**2 - b**2) == c**2):
        print("right")
    else:
        print("wrong")
    a, b, c = map(int, input().split())
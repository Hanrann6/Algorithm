import sys
n = input()
num = list(map(int, sys.stdin.readline().split()))
print(min(num), max(num))
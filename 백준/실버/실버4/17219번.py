import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwd = dict()
for _ in range(n):
    site, password = input().split()
    pwd[site] = password

for _ in range(m):
    site = input().rstrip()
    print(pwd[site])
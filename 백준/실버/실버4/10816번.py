import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
cset = set(card)
clist = {} # 숫자, 개수 포함 딕셔너리
for c in cset:
    clist[c] = 0

for c in card:
    clist[c] += 1

m_num = int(input())
mlist = list(map(int, input().split()))
ans = []

for m in mlist:
    if m not in clist.keys():
        print(0, end=' ')
    else:
        print(clist[m], end=' ')

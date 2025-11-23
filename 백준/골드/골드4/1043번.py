import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split()) #사람 수, 파티 수
people = [i for i in range(n+1)] #사람
host = [i for i in range(n+1)] #주인

def union(a, b): #합체
    p = find(a)
    q = find(b)
    if(p == q):
        return
    else:
        host[q] = p

def find(a): #주인 원소 찾기
    if (host[a] == a):
        return a
    else:
        host[a] = find(host[a])
        return host[a]


#진실을 아는 사람 정보
know = list(map(int, input().split()))
know_n = know[0]
if(know_n == 0): #아는 사람 없으면 파티 전부 가능
    print(m)
    exit()
else:
    for i in range(1, know_n):
        union(people[know[i]], people[know[i+1]])

#파티 정보 - union
party_list = [[] for _ in range(m)]
for i in range(m):
    party = list(map(int, input().split()))
    party_list[i].extend(party)
    if party[0] == 1:
        continue
    else:
        for j in range(1, party[0]):
            union(people[party[j]], people[party[j+1]])


cnt = 0 #가능한 파티 개수
t = find(know[1]) #진실을 아는 쪽의 host
for party in party_list:
    can = 1
    for i in range(1, party[0] + 1):
        if find(party[i]) == t:
            can = 0
            break
    if can == 1:
        cnt += 1


print(cnt)
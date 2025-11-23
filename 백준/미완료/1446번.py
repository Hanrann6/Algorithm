#1446번 - 실버1
#왜인지.. 틀렸다고 한다ㅠ
import sys

n, ans = map(int, sys.stdin.readline().strip().split())
d_list = [] #절약거리 리스트
p_list = [] #시작, 끝 점 리스트

for _ in range(n):
    start, fin, dis = map(int, sys.stdin.readline().split())
    d = fin - start - dis
    if(d < 0 or fin > ans):
        start = 0
        fin = 0
        d = 0
    d_list.append(d)
    p_list.append(start)
    p_list.append(fin)

for _ in range(n):
    d_max = max(d_list)
    index = d_list.index(d_max)
    d_list[index] = 0
    i=0
    sum=0
    save=[]
    if(p_list[2*index]!=0 or p_list[2*index+1]!=0):
        ans -= d_max
        for k in range(len(p_list)//2):
            if(i == 2*index or (i+1) == 2*index+1):
                i += 2
                continue
            if(p_list[i]==0 and p_list[i+1]==0):
                i += 2
                continue
            if ((p_list[i]>=p_list[2*index] and p_list[i] < p_list[2*index+1]) or (p_list[i+1]>p_list[2*index] and p_list[i+1] <= p_list[2*index+1])):
                sum += d_list[i//2]
                save.append(i)
                save.append(i+1)
                p_list[i] = 0
                p_list[i+1] = 0
            i += 2
        if(sum > d_max):
            ans = ans + d_max - sum
            for t in range(len(save)):
                d_list[save[t]//2] = 0
                p_list[save[t]] = 0

print(ans)
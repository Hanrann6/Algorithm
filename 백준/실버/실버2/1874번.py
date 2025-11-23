import sys
input = sys.stdin.readline

n = int(input())
num = []
seq = [0]
ans=[]
count=1 #숫자 포인터
for i in range(n): #수열 받기
    num.append(int(input()))
num = num[::-1]

for _ in range(n):
    p = num.pop()
    if (p > seq[-1]):
        if (p < count):
            ans.clear()
            ans.append('NO')
            break
        while(p > seq[-1]):
            ans.append('+')
            seq.append(count)  # 1 2 3
            count += 1
    elif (p < seq[-1]):
        seq.pop()
        ans.append('-')
    if(p==seq[-1]):
        seq.pop()
        ans.append('-')


print('\n'.join(ans))

'''
실버2, 성공
12345678
1235
43687
'''


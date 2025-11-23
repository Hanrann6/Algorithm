import sys
n = int(sys.stdin.readline())
ans=0
for _ in range(n): #단어 1개씩 돌기
    word = sys.stdin.readline()
    wlist = []
    k = ''
    is_pass = True
    for i in word: #단어의 1글자씩 돌기
        if(k==i):
            continue
        elif(i not in wlist):
            wlist.append(i)
        else:
            is_pass = False
            break
        k = i  # 직전 문자 저장용
    if is_pass:
        ans += 1

print(ans)
#실버 5, 성공
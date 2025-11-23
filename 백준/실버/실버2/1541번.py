import sys
line = sys.stdin.readline().strip()
num = []
number = ''
for i in line: #식 띄어서 num에 저장
    if i == '+' or i == '-':
        if number != '':
            num.append(number)
            number = ''
        num.append(i)
    else:
        if number == '' and i == '0':
            continue
        number += i
if number != '':
    num.append(number)

total = [num[0]]

for i in range(0, len(num)-1, 2): #덧셈은 계산한 결과를 total에 저장
    a, b = num[i+1], num[i+2]
    if a == '-':
        total.append(a)
        total.append(b)
    if a == '+':
        total[-1] = int(total[-1]) + int(b)


ans = int(total[0])
for i in range(0, len(total)-1, 2): #계산
    a, b = total[i+1], int(total[i+2])
    if a == '-':
        ans -= b
    else:
        ans += b

print(ans)
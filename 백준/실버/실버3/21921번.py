import sys
input = sys.stdin.readline

n, x = map(int, input().split())
num = list(map(int, input().split()))

sum_num = sum(num[:x])
max_num = sum_num
slist = [max_num]
for i in range(n-x):
    sum_num -= num[i]
    sum_num += num[i+x]
    if(max_num < sum_num):
        max_num = sum_num
    slist.append(sum_num)

if(max_num==0):
    print('SAD')
else:
    print(max_num)
    count = 0
    for i in slist:
        if (i == max_num):
            count += 1
    print(count)


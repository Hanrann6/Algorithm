f = int(input())
n = 1
for i in range(f, 0, -1):
    n *= i

s = str(n)[::-1]
cnt = 0
for i in s:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)

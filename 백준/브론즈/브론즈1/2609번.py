a, b = map(int, input().split())

# 최대 공약수
mini = 1
for i in range(2, b+1):
    if (a % i == 0) and (b % i == 0):
        mini = i

print(mini)

# 최소 공배수
aa = a // mini
bb = b // mini
print(aa*bb*mini)
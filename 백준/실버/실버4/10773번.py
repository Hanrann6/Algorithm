#10773번
import sys
myque = []
k = int(sys.stdin.readline())

for _ in range(k):
    n = int(sys.stdin.readline())
    if(n!=0):
        myque.append(n)
    else:
        myque.pop()

sum=0
for i in range(len(myque)):
    sum = sum + myque[i]

print(sum)
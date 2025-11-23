import sys
myque = []
n = int(sys.stdin.readline()) #버퍼 사이즈
while True:
    k = int(sys.stdin.readline())
    if(k==-1): break
    if(k==0):
        myque.pop(0)
    elif(len(myque)<n):
        myque.append(k)

print(*myque)
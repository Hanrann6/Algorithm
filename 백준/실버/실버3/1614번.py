#1614번 - 실버 3
import sys
finger = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if(finger == 1 or finger == 5):
    print(8 * n + (finger - 1))
elif(finger == 3):
    print(4 * n + 2)
elif(finger == 2):
    if(n % 2 == 1):
        print(4*n+3)
    else:
        print(4*n+1)
elif(finger == 4):
    if (n % 2 == 1):
        print(4 * n + 1)
    else:
        print(4 * n + 3)
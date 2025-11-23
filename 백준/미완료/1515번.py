#1515번 - 실버 3
#계속 런타임 에러..
import sys
num = list(sys.stdin.readline())
for i in range(1050):
    if (i < 10):
        if (i == int(num[0])):
            num.pop(0)
    elif (i < 100):
        if (i//10 == int(num[0])):
            num.pop(0)
            if not num:
                n = i
                break
        if (i % 10 == int(num[0])):
            num.pop(0)
    elif (i < 1000):
        if (i//100 == int(num[0])):
            num.pop(0)
            if not num:
                n = i
                break
        if ((i % 100) // 10 == int(num[0])):
            num.pop(0)
            if not num:
                n = i
                break
        if (i % 10 == int(num[0])):
            num.pop(0)
    else:
        if (i // 1000 == int(num[0])):
            num.pop(0)
            if not num:
                n = i
                break
        if ((i % 1000) // 100 == int(num[0])):
            num.pop(0)
            if not num:
                n = i
                break
        if ((i % 100) // 10 == int(num[0])):
            num.pop(0)
            if not num:
                n = i
                break
        if (i % 10 == int(num[0])):
            num.pop(0)
    if not num:
        n = i
        break
print(n)
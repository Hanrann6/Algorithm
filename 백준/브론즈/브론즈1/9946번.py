#9946번
import sys

n = 1
while True:
    ans = sys.stdin.readline().strip()
    test = sys.stdin.readline().strip()
    if ans == "END":
        break
    if(len(ans)!=len(test)):
        print(f"Case {n}: different")
        n += 1
        continue
    for i in range(len(test)):
        c = test[i]
        if c in ans:
            index = ans.find(c)
            ans = ans[:index] + ans[index+1:]
        else:
            print(f"Case {n}: different")
            n += 1
            break
    if(ans == ''):
        print(f"Case {n}: same")
        n += 1
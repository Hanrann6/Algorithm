# 1003번 - 실버 3
import sys

n = int(sys.stdin.readline())
num = []
f_dict = {
    0: [1, 0],
    1: [0, 1]
}
new_key = 2
new_value = [0, 0]

for _ in range(39):
    li1 = f_dict[new_key-2]
    li2 = f_dict[new_key-1]
    new_value[0] = li1[0] + li2[0]
    new_value[1] = li1[1] + li2[1]
    f_dict[new_key] = list(new_value) #왜인지 여기 list를 붙여 줘야 잘 돌아감
    new_key += 1

for _ in range(n):
    k = int(sys.stdin.readline())
    print(*f_dict[k])
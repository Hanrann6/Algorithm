word = input().rstrip().upper()
d = dict()
for s in word:
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1

if len(d) == 1:
    print(*d.keys())
else:
    # 내림차순 정렬 리스트
    sorted_d = sorted(d.items(), key=lambda x: -x[1])
    a1, a2 = sorted_d[0]
    b1, b2 = sorted_d[1]
    if a2 == b2:
        print('?')
    else:
        print(a1)

k = 1
while k != 0:
    num_list = list(map(int, input().split()))
    k = num_list[0]
    lotto = num_list[1:]
    n1, n2, n3, n4, n5, n6 = lotto[:6]
    # 미완
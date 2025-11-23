import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    s = list(map(int, input().split()))
    graph.append(s)

ans = [0, 0] # 0 개수, 1 개수


def dfs(x, y, l):
    if l == 1: # 변의 길이가 1이면
        if graph[y][x] == 0:
            ans[0] += 1
        else:
            ans[1] += 1
        return
    # 변의 길이가 2 이상
    isOne = False
    isZero = False
    for i in range(x, x+l):
        for j in range(y, y+l):
            if graph[j][i] == 0:
                isZero = True
            if graph[j][i] == 1:
                isOne = True

    if isZero and isOne: # 혼합
        l //= 2
        dfs(x, y, l)
        dfs(x+l, y, l)
        dfs(x, y+l, l)
        dfs(x+l, y+l, l)
    elif isZero:
        ans[0] += 1
        return
    elif isOne:
        ans[1] += 1
        return


dfs(0, 0, n)
print(ans[0])
print(ans[1])
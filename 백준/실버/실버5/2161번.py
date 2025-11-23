import queue

que = queue.Queue()
li = []
n = int(input())

for i in range(1, n+1): #거꾸로 순서로의 범위
    que.put(i)

for _ in range(n-1):
    q = que.get()
    li.append(q) # 버린 거 리스트에 추가
    p = que.get()
    que.put(p) # 큐 위에 올리기

print(*li, que.get())
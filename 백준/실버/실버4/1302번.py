import sys
input = sys.stdin.readline

n = int(input())
books = dict()
for _ in range(n):
    book = input()
    if book not in books.keys():
        books[book] = 1
    else:
        books[book] += 1

ans = sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(ans[0][0])

import sys
input = sys.stdin.readline

n = int(input())
words = set()
for _ in range(n):
    word = input().strip()
    words.add((len(word), word))

words = list(words)
words.sort()

for i in range(len(words)):
    print(words[i][1])
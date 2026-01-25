import sys
input = sys.stdin.readline

# 우선순위: 등장수, 길이, 알파벳
n, m = map(int, input().split())
words = dict()
for _ in range(n):
    word = input().strip()
    if(len(word) < m):
        continue
    else: # 단어 길이 이상만
        if(word not in words.keys()):
            words[word] = [1, len(word)]
        else:
            words[word][0] += 1

ans = sorted(words.items(), key = lambda x:(-x[1][0], -x[1][1], x[0]))
for a in ans:
    print(a[0])
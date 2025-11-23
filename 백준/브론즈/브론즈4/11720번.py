import sys
n = sys.stdin.readline() #사용 안 함
nlist = list(sys.stdin.readline())
nlist.pop() # 마지막 요소 /n 제거
nlist = list(map(int, nlist)) # int 형변환
print(sum(nlist)) # 합 출력
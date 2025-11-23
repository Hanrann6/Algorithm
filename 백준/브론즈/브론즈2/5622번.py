str=input()
sum=0
list=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for s in str:
    for k in range(len(list)):
        if s in list[k]:
            sum += (k+3)

print(sum)

'''
s = input()
sum=0

for c in s:
    if 'A' <= c <= 'C':
        sum += 3
    elif 'D' <= c <= 'F':
        sum += 4
    elif 'G' <= c <= 'I':
        sum += 5
    elif 'J' <= c <= 'L':
        sum += 6
    elif 'M' <= c <= 'O':
        sum += 7
    elif 'P' <= c <= 'S':
        sum += 8
    elif 'T' <= c <= 'V':
        sum += 9
    elif 'W' <= c <= 'Z':
        sum += 10

print(sum)
'''
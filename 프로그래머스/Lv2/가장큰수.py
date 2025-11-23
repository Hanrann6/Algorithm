numbers = [8, 3, 30, 34, 5, 9]

def solution(numbers):
    l = len(numbers)
    for i in range(0, l):
        numbers[i] = str(numbers[i])
    numbers.sort()
    print(numbers)
    numbers.reverse()
    answer = ''
    for i in numbers:
        answer += i
    print(answer)
    return answer

solution(numbers)

# 첫재자리가 큰 순서대로, 둘째자리 -- 비교
# sort, key 사용
'''
먼저 리스트의 각 멤버를 str 형식으로 만든다
각 문자열의 [0], [1],, 기준으로 정렬한다
비어있는 경우는? 9로 처리
[0]으로 비교하면 -> 9, 5, 3, 30, 34
[1]로 비교하면 -> 9, 5, 3, 34, 30
-> 9533430
[9, 294, 4, 43, 49, 590, 80]
첫째자리를 기준으로 리스트 분리 [294], [415, 4, 43, 49], [590], [80], [9]

'''
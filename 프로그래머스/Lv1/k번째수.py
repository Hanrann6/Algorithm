commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]

def solution(array, commands):
    answer = list()
    for comm in commands:
        i, j, k = comm
        array_c = array[i - 1:j]  # 자른 배결
        array_c.sort()
        ans = array_c[k - 1]
        answer.append(ans)

    print(answer)
    return answer

solution(array, commands)
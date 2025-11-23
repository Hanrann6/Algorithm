#프로그래머스 스택/큐-같은 숫자는 싫어
#답은 모두 맞았으나 효율성에서 실패한 코드
import queue
def solution(arr):
    answer = []
    que = queue.Queue()
    for i in arr:
        que.put(i)

    q = que.get()
    answer.append(q)

    for _ in range(que.qsize()):
        p = que.get()
        if q != p:
            q = p
            answer.append(q)

    return answer

#다른 답 참고함
def solution(arr):
    answer=[]
    for i in arr:
        if answer[-1:]!=[i]: #answer을 슬라이싱하면 리스트를 리턴하기 때문에 비교값으로 i도 리스트로 만들어 줘야됨
            answer.append(i)
    return answer
#효율성도 통과!

#프로그래머스 스택/큐-프로세스
#if문에 any라는 것이 있다.
#enumerate 함수 사용-> queue에 튜플 저장
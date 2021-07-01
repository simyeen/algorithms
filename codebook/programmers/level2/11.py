
from collections import deque

def solution(priorities, location):
    answer = 0

    q = deque()
    stack = sorted(priorities) # 우선순위를 위한 스택
    for i in range(len(priorities)): # 인덱스랑 같이 튜플로 저장
        q.append((priorities[i], i))
    qe = [(i,p) for i,p in enumerate(priorities)] # range대신 사용
    print(qe)

    order = []
    while q:
        pri, index = q.popleft()
        if pri == stack[-1] : 
            order.append(index)
            stack.pop()
        else : 
            q.append((pri, index))

    return order.index(location) + 1

print(solution([2, 1, 3, 2],2))
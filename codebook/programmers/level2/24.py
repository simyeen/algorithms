from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = bridge_length
    wait = deque()
    for i in truck_weights:
        wait.append(i)

    cnt = 0
    stack = []
    while wait:
        cur = wait.popleft()
        stack.append(cur)
        if sum(stack) <= weight:



    return answer


print(solution(2,10,[7,4,5,6]))
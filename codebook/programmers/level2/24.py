from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = bridge_length
    wait = deque()
    for i in truck_weights:
        wait.append(i)

    cnt = 0
    queue = deque()
    while wait:
        if len(wait) != 0 :
            cur = wait.popleft()

        queue.append(cur)
        if sum(queue) <= weight: # 스택에 최대한 꽉 담기
            continue
        wait.append(cur) # 마지막에 못 들어간 차량 다시 넣어주기

        queue.popleft() # 빠져나가는 차량 발생.    
        cnt += time

        



    return cnt


print(solution(2,10,[7,4,5,6]))
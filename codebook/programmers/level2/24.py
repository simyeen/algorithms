from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    size = bridge_length

    start_list = deque(truck_weights)
    bridge_list = deque()
    end_list = deque()

    while len(end_list) != len(truck_weights):
        if len(bridge_list)==0 and start_list :
            bridge_list.append((start_list.popleft(),cnt))
            cnt += 1
            continue

        if bridge_list: # 나가는 트럭 검사
            if bridge_list[0][1]+size == cnt: 
                truck, trash = bridge_list.popleft()
                end_list.append(truck)

        if start_list: # 들어오는 트럭 검사
            truck = start_list.popleft()

            sum_value = 0
            for value, time in bridge_list: sum_value += value

            if sum_value + truck <= weight:
                bridge_list.append((truck,cnt))
            else : start_list.appendleft(truck)

        cnt += 1

    return cnt
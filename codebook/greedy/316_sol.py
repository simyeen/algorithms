import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i],i+1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식의 시간
    length = len(food_times) # 남은 음식의 개수

    while sum_value + ((q[0][0]-previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length    
        previous = now
    result = sorted(q, key = lambda x : x[1])
    return result[(k-sum_value) % length][1]

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times,k))



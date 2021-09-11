from collections import deque

def solution(food_times, k):
    if sum(food_times) <= k : return -1
    if len(food_times) >= k : return k

    tmp_times, n = [], len(food_times)
    for i, time in enumerate(food_times): tmp_times.append([time,i+1])
    tmp_times.sort()
    times = deque()
    for time in tmp_times: times.append(time)

    while k//n >= times[0][0] and n > 0: # 몫만큼 빼주기.
        min_value = times[0][0]
        if k//n >= min_value:
            times.popleft() # 잘가 min아
            for _ in range(n-1):
                value, index = times.popleft() 
                value -= min_value
                if value > 0: times.append([value,index])
            k -= n*min_value
            n = len(times)   
            if n == 0 : return -1         
        else : break # 나머지들만 존재.
    print(k, times)
    return times[k][1]

food_times = [1,1,1]
k = 5
print(solution(food_times, k))

# 한큐 돌릴 때 전체 감소 => k//len 만큼 
# 1. 5 6 7 8 9         => if 34//5 >= min 면 우선 min만큼 전체 차감시키기.
# 2. 0 1 2 3 4         => k -= n*min(34-25)로 변신.
# 3. 0은 전부다 빼버리고 n==0이면 종료. 1, 2, 3, 4  => k = 9로 다시 보자잉
# 4, 1 2 3 4           => if 9//4 >= 1 면 min 만큼 전체 차가시키기.
# 5. 0 1 2 3.          => k -= n*min(4*1) (9-4)
# 6. 1, 2, 3           => k = 5로 다시보자.
# 7. 1 2 3             => if 5//3 >= 1이니까
# 8. 1, 2              => k = 2 인데 아직 if k//2 >= 1
# 5. 1                 => if k=0 >= min이 깨져서 탈출.
# 6. 남은 배열중 arr[k]가 답일듯.

def solution(food_times, k):
    answer = 0
    now = 0

    for _ in range(k):
        
        now %= len(food_times)
        print(now, food_times)
        if food_times[now] >=1 :
            food_times[now] -= 1
            now += 1
            continue
        else :
            cnt = 0
            for j in range(now, now + len(food_times)):
                if food_times[j] >= 1:
                    food_times[j] -= 1
                    now = j + 1
                    break
                else :
                    cnt += 1
                    now += 1
                    if cnt == len(food_times):
                        return -1

    return now


food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))
print(food_times)
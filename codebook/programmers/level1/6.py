from itertools import combinations


nums = [3, 3, 3, 2, 2, 4]

def solution(nums):
    answer = 0

    max_value = len(nums) // 2
    target_len = len(set(nums))

    if target_len >= max_value:
        answer = max_value
    else :
        answer = target_len

    return answer


print(solution(nums))
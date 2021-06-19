from itertools import combinations



def solution(nums):
    answer = 0

    candidates = set(combinations(nums, len(nums)//2))

    max_value = -1e9
    for pokmons in candidates :
        target = len(set(pokmons))
        max_value = max(max_value, target)
    
    answer = max_value
    return answer


print(solution(nums))
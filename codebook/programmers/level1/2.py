from itertools import combinations

nums = [1,2,7,6,4]

def solution(nums):
    answer = 0

    count = 0
    for combi in combinations(nums ,3):
        target = sum(combi)
        check = False
        for i in range(2, target):
            if target % i == 0 :
                check = True
                break
        
        if not check :
            count += 1
            
    answer = count
    return answer

print(solution(nums))
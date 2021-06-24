from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    total = sum(numbers)
    for i in range(1, len(numbers)+1):
        combi = (list(combinations(numbers,i)))
        for c in combi :
            if total - 2*sum(c) == target:
                answer +=1
    return answer

print(solution([1,1,1,1,1],3))
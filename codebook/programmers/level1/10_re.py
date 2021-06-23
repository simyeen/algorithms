from itertools import combinations

def solution(d, budget):
    answer = 0
    d = sorted(d)
    
    for i in d:
        if budget - i >= 0:
            budget -= i
            answer += 1 

    return answer

print(solution([1,3,2,5,4], 9))
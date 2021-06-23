from itertools import combinations

def solution(d, budget):
    answer = []

    for i in range(1,len(d)+1):
        data = list(combinations(d, i))
        for c in data:
            if sum(c) == budget:
                answer.append(i)
    answer = max(answer)
    return answer

print(solution([1,3,2,5,4], 9))
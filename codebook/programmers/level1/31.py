from itertools import combinations

def solution(numbers):
    answer = []
    
    combination = list((combinations(numbers, 2)))
    for i in combination :
        print(i)
        answer.append(sum(i))
    
    answer = sorted(list(set(answer)))

    return answer

print(solution([2,1,3,4,1]))
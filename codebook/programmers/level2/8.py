from itertools import permutations

def solution(numbers):
    answer = []
    n = len(numbers)
    
    com = list(permutations(numbers, n))
    
    for c in com :
        tmp = ''
        for i in c:
            tmp += str(i)
        answer.append(int(tmp))

    return max(answer)
    

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))


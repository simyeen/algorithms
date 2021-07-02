def solution(numbers):
    answer = []
    
    for n in numbers:
        i = 1
        while True:
            cnt = bin(n^(n+i)).count('1')
            if cnt <= 2:
                answer.append(n+i)
                break
            i += 1

    return answer


numbers = [2,7]
print(solution(numbers))

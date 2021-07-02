def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        tmp = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                tmp += 1
        answer.append(tmp)
        
    answer.append(0)
        
    print(int('10',2))
    return answer

print(solution([1, 2, 3, 2, 3]))

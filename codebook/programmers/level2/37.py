def solution(prices):
    answer = [0 for _ in prices]

    for i in range(len(prices)):    
        tmp = prices[i:] 
        cnt = 0
        while len(tmp) != 1:
            if tmp[0] <= tmp[-1]:
                cnt += 1
            tmp.pop()
                
        answer[i] = cnt
        
    return answer

print(solution([1, 2, 3, 2, 3]))
def solution(prices):
    answer = [0 for _ in prices]

    for i in range(len(prices)-1):
        down = False
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j] : # 하락장 일때
                if down == False : answer[i] += 1
                down = True
            elif prices[i] == prices[j] and down == False:
                answer[i] += 1
            elif prices[i] < prices[j] :
                down = False
                answer[i] += 1 
                
    return answer
    

print(solution([1, 2, 3, 2, 3, 1]))

# 한참 헤매다가 다른분 설명보고이해 했네요.

# prices = {1, 2, 3, 2, 3, 1} return {5, 4, 1, 2, 1, 0}

# 이 테스트케이스가 왜 저렇게 떨어지는지 한 번 따라가보시고 해보시면 금방 이해하실꺼에요~

# 테스트케이스 입출력 설명 예 중

# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.


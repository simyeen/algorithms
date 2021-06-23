import math 

def solution(n):

    sqrt = n ** (1/2)  # 소수점
    print(sqrt)
    print(sqrt % 1)
    if sqrt % 1 == 0: 
        
        return (sqrt + 1) ** 2

print(solution(9))
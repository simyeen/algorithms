from itertools import combinations

def solution(numbers):
    answer = 0
    
    num = list(numbers)
    
    for i in range(1,len(num)+1):        
        combi = list(combinations(num,i)) # 3C2
        for c in combi: # 3개중 하나의 조합
            
            tmp = ''
            for i in c: # 조합
                tmp += i
            
            target = int(tmp)
            print(target)
        
            for i in range(2, target-1):
                if target % i == 0 : break
            else : answer += 1 
    
    return answer

print(solution("011"))
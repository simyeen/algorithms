from itertools import combinations

def solution(clothes):
    answer = 0
    
    d = dict()
    for clo in clothes:
        d[clo[1]] = 0
    for clo in clothes:
        d[clo[1]] += 1
    
    
    for i in range(1,len(d)+1):
        combi = list(combinations(d,i))
        for c in combi:
            tmp = 1
            for j in c:
                tmp *= d[j]
            answer += tmp
    return answer
    


clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
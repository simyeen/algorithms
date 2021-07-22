from itertools import combinations

def solution(number, k):
    answer = ''
    
    index = list(combinations(range(len(number)),k))
    
    max_value = -1e9
    for i in index :
        tmp = 0
        for j in range(len(number)):
            if j in i: continue
            tmp += number[j]
        max_value = max(tmp, max_value)
                

    return str(max_value)
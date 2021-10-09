import heapq
from itertools import product

def solution(word):

    q = []
    heapq.heappush(q,1)
    print(q)


    arr = []
    for i in range(1,6): 
        for pro in product(['A','E','I','O','U'],repeat = i): arr.append(''.join(pro))
        
    arr.sort()
    return arr.index(word)+1
    
        
print(solution('I'))
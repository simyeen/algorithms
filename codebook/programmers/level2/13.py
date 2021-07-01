from itertools import combinations

def solution(brown, yellow):
    ylist = []
    
    if yellow == 1: return [3,3]
    
    i = 1
    while yellow != 1: # yellow의 약수 구하기
        if yellow % i == 0:
            ylist.append(i)
            yellow //= i 
            i = 2
        else : i += 1 
    
    arr = [i for i in range(len(ylist))]
    for i in range(1, len(ylist)//2+1): 
        for row in combinations(arr, i): # row가 될만한 애들의 index
            x, y = 1, 1 
            for j in arr:
                if j in row : 
                    x *= ylist[j]
                else :
                    y *= ylist[j]
            r, c = max(x,y), min(x,y)
            if 2*(r+2 + c) == brown :
                return [r+2, c+2]
    
    return ylist

brown = 10
yellow = 2
print((solution(10,2)))
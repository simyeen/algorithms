from math import gcd

def solution(w,h):
    check = 0
    answer = 0 
    total = w*h
    
    g = gcd(w,h)
    print(g)
    row, col = w//g, h//g
    print(row,col)
    for i in range(1, row+1):
        if i == row:
            check += col-(row*(i-1) - (i-1))
        else : check += row
    
    check *= g
    answer = total - check
    
    return answer

print(solution(8,12))
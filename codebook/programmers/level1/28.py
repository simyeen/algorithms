def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6 :
        for c in s:
            print(c)
            if c == ' ' : continue
            if not c.isdigit():
                answer = False
    
    else : answer = False
    
    return answer

s = '1234 a1234'

print(solution(s))
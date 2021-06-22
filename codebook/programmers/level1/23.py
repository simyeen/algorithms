def solution(s):
    answer = 0

    minus = True if s[0] == '-' else False
    
    if s[0] == '-':
        return -int(s[1:])
    else : return int(s)
        
    


print(solution('-123412'))
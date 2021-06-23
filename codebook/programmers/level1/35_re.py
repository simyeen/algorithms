def solution(dartResult):
    answer = 0


    for i in dartResult:
        
        if i.isdigit() :
            tmp = i
            continue

        elif i == 'S':
            continue
        elif i == 'D':
            tmp **= 2
            continue
        elif i == 'T':
            tmp **= 3
            continue
        elif i == '*':
            
        elif i == '#':
        


    return answer

print(solution("1S2D*3T"))
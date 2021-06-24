def solution(dartResult):
    answer = 0
    d = dartResult    
    for i in range(len(d)):       
        if d[i].isdigit() :
            if d[i+1].isdigit():
                tmp = 10
                d = d.replace('0','K')
            else : tmp = int(d[i]) 
        elif d[i] == 'D':
            tmp **= 2
        elif d[i] == 'T':
            tmp **= 3
        elif d[i] == '*':
            answer *= 2
        elif d[i] == '#':
            answer -= tmp

        answer += tmp
        print(d[i], tmp, answer)
    print(d)
    return answer

print(solution("1D2S#10S"))
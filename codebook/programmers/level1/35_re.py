def solution(dartResult):
    answer = 0
    d = dartResult
    for i in range(len(d)):
        
        if d[i]== '0' : continue

        if d[i].isdigit() :
            if d[i+1].isdigit():
                tmp = 10
            tmp = int(d[i])
            continue

        elif d[i] == 'S':
            answer += tmp
        elif d[i] == 'D':
            tmp **= 2
            answer += tmp
        elif d[i] == 'T':
            tmp **= 3
            answer += tmp
        elif d[i] == '*':
            answer *= 2
        elif d[i] == '#':
            answer = -answer
        print(answer)
    return answer

print(solution("1D2S#10S"))
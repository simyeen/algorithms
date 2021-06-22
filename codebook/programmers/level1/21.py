def solution(s):

    answer = ''
    cur = 0
    for char in s:
        if char == ' ' : 
            answer += char
            cur = 0
            continue
        tmp = ""
        if cur % 2 == 0 :
            answer += char.upper()
        else : 
            answer += char.lower()        
        cur += 1

        answer += tmp

    return answer
    

print(solution("try hello world"))
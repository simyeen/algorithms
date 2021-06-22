def solution(s, n):
    answer = ''    

    for c in s:
        print(c)
        if c == ' ':
            answer += ' '
            continue
        tmp = ''
        target = ord(c) + n
        if c.islower():    
            if target > ord('z'):
                tmp += (chr(target-26))
            else : tmp += (chr(target))
        else :
            if target > ord('Z'):
                tmp += (chr(target-26))
            else : tmp += chr(target)
        answer += tmp

    return answer

print(solution("a B z       Aaa" ,7))

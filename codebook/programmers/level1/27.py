def solution(s):
    answer = ''
    
    as_list = []
    for c in s:
        as_list.append(ord(c))
    as_list = sorted(as_list, reverse=True)
    as_list = map(chr, as_list)
    answer = ''.join(as_list)
    
    return answer

print(solution("Zbcdefg"))
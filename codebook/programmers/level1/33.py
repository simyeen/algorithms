def solution(s):
       
    check1, check2 = 0, 0
    
    for char in s:
        if char == 'p' or char == 'P' : check1 += 1
        elif char == 'y' or char == 'Y' : check2 += 1
    if check1 != check2 : return False

    return True

print(solution("PYY"))
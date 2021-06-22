def solution(x):
    answer = True
    
    target = str(x)
    num = 0
    
    for i in range(len(target)):
        num += int(target[i])

    if (x % num)  == 0:
        answer = True
    else : answer = False
    
    return answer

print(solution(18))
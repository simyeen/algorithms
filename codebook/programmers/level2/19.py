def solution(numbers):
    answer = []
    test = []
    
    for n in numbers:
        target = bin(n)[2:]
        index = target.rfind('0')
        test.append(index)
        if index != -1: # 제일 마지막 1전에 0이 존재할때
            target = target[:index] + '1' + target[index+1:]
            answer.append(int(target,2))
        else :
            if int(target,2) == 1 : answer.append(2)
            elif int(target,2) == 3: answer.append(5)  
            else:
                target = '10'+ '1'*(len(target)-1)
                answer.append(int(target,2))
    return answer

print(solution([5,15,31,63]))
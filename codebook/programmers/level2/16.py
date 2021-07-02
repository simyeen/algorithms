def solution(numbers):
    answer = []
    
    for n in numbers:
        target = bin(n)[2:]
        index = target.rfind('0')

        if index != -1:
            target = target[:index] + '1' + target[index+1:]
            answer.append(int(target,2))
        else :
            target = '1' + '0'*len(target)
            answer.append(int(target,2)+3)

    return answer

numbers = [2,7]
print(solution(numbers))


s = ['[',']']
print(s[-1:])
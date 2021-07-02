def solution(numbers):
    answer = []
    
    for n in numbers:
        target = bin(n)[2:]
        index = target.rfind('0')
        print(target,index)

        if index != -1:
            target = target[:index] + '1' + target[index+1:]
            answer.append(int(target,2))
        print(target)
    return answer

numbers = [2,7]
print(solution(numbers))



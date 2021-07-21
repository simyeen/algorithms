from itertools import permutations

def solution(numbers):
    answer = []
    nums = [str(i) for i in numbers]

    lenlist = [[] for _ in range(max(numbers)+1)]
    for num in nums:
        lenlist[int(num)].append(len(num))

    # 맨 앞자리가 같다면 
    #34 30 3 
    # 이럴 떄 는 34 3 30 이 된다 => 
    # 바로 뒷자리가 앞자리 보다 큰애(큰애들도 크기순) | 앞자리 | 앞자리보다 작은애(애내는 크기 순)


    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))


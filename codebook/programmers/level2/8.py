from itertools import permutations

def solution(numbers):
    answer = []
    nums = [str(i) for i in numbers]
    mylist = [[] for _ in range(10)]

    for i in nums:
        mylist[int(i[0])].append(int(i))
    for per in mylist:
        if len(per) < 2 : 
            if len(per) == 1 :
                answer.append(per[0])
            continue
        
        com = list(permutations(per, len(per)))
        tmplist = []
        for c in com:
            tmp = ''
            for i in c:
                tmp += str(i)
            tmplist.append(int(tmp))
        answer.append(max(tmplist))
            
    k = ''
    for i in range(len(answer)-1, -1, -1) :
        k += str(answer[i])

    return k

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))


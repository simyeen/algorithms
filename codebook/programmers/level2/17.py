from itertools import permutations

def solution(numbers):

    num = list(numbers)
    target = set()
    for i in range(1, len(num)+1):
        mylist = set(list(permutations(num,i)))
        for per in mylist:
            tmp = ''
            for i in per :
                tmp += i
            target.add(int(tmp))
    cnt = 0     
    for i in target:
        if i < 2 : 
            continue
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0 : break
        else : cnt += 1        

    return cnt

print(solution("013"))

import math 

def solution(n):

    target = math.sqrt(n)
    target_pow1 = float((n+1)**2)
    target_pow2 = (target+1)**2

    print(target_pow1, target_pow2)
    if target_pow1 == target_pow2:
        print(11)
        return (target+1)**2
    else :
        return -1
    # if isinstance(target, int):
    #     return (target+1)**2
    # else :
    #     return -1

print(solution(121))
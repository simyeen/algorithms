n = 3
lost = [3]
reserve = [1]

def solution(n, lost, reserve):
    answer = 0

    check = [False]
    for _ in range(n):
        check.append(True)
    for lo in lost:
        check[lo] = False
        for re in reserve:
            if lo == re:
                reserve.remove(re)
                
    print(check)
    for re in reserve:
        if re == 1:
            check[re+1] = True
        elif re == n:
            check[re-1] = True
        else:
            if check[re-1] == False:
                check[re-1] = True
            else :
                check[re+1] = True

    print(check)
    for i in check:
        if i == True:
            answer += 1

    return answer

print(solution(n, lost, reserve))
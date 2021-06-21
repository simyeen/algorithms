n = 5
lost = [1,2,4,5]
reserve = [3]

def solution(n, lost, reserve):
    answer = 0

    check = [False]
    for _ in range(n):
        check.append(True)
    for lo in lost:
        check[lo] = False
        for re in reserve:
            if lo == re:
                check[re] = True
                reserve.remove(re)

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

    for i in check:
        if i == True:
            answer += 1

    return answer

print(solution(n, lost, reserve))
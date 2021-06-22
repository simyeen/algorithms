def solution(n):

    n = str(n)
    return [int(i) for i in n[-1::-1]]


print(solution(12345))

# 끝에서부터 하고 싶으면 그냥 n[::-1]로만 해도 된다.
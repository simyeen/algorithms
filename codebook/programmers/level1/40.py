def solution(n, arr1, arr2):
    answer = ['#'* n]*n 
    secret_map = []

    for i, j in zip(arr1, arr2):
        secret_map.append(str(int(bin(i)[2:]) + int(bin(j)[2:])))

    for i in range(len(secret_map)):
        if len(secret_map[i]) != n :
            secret_map[i] = ('0'*(n-len(secret_map[i]))) + secret_map[i]
        for j in range(len(secret_map[i])):
            if secret_map[i][j] == '0':
                answer[i] = answer[i][:j] + ' ' + answer[i][j+1:]
                
    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
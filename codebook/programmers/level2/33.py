def solution(arr): # 로직 오류
    answer = 0
    tmp = []
    arr.sort()
    j = 2
    while True:
        if 1 in arr : break
        if j > arr[len(arr)-1] : break
        cnt = 0 
        for i in range(len(arr)):
            if arr[i] % j == 0:
                cnt += 1
        if cnt == 4:
            tmp.append(j)
            for i in range(len(arr)):
                arr[i] = arr[i]//j
            j = 2
        else : j+= 1

    print(tmp, arr)
            
    ans = 1
    for i in tmp : ans *= i
    for i in arr : ans *= i
        
    return ans
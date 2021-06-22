def solution(arr):
    answer = []

    cur = arr[0]
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        else : 
            answer.append(arr[i])
    answer.append(arr[-1])


    return answer

print(solution([1,1,3,3,0,1,1]))
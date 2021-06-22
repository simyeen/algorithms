arr1 = [[1,2],[2,3]]	
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = [[]]
    
    row = len(arr1)
    col = len(arr1[0])
    for _ in range(row-1):
        answer.append([])

    for i in range(row):
        for j in range(col):
            answer[i].append(arr1[i][j] + arr2[i][j])
    
    return answer

print(solution(arr1,arr2))
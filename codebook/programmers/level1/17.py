def solution(arr):
    
    min_value = 1e9
    for i in range(len(arr)):
        min_value = min(min_value, arr[i])
    arr.remove(min_value)
    
    if arr: return arr
    else : return [-1]
    
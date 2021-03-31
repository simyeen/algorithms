def binSearch(arr, target) :
    start, end = 0, n-1

    while start <= end :
        mid = (start+end)//2
        if arr[mid] == target : 
            return mid
        if arr[mid] > target : 
            end = mid-1
        elif arr[mid] < target :
            start = mid+1
    return None
        
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binSearch(arr, target)
if result == None:
    print('no item')
else :
    print(result + 1)
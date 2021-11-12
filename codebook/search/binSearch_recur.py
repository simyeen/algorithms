def binSearch(arr, target, start, end) :
    if start >= end :
        return None

    mid = (start + end)//2
    if arr[mid] == target :
        return mid # index를 return한다.
    if arr[mid] > target :
        return binSearch(arr, target, start, mid-1)
    elif arr[mid] < target :
        return binSearch(arr, target, mid+1, end)
        
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binSearch(arr, target, 0, n-1)
if result == None:
    print('no item')
else :
    print(result + 1)
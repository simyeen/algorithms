# def b_search(arr, target):
#     start, end = 0, len(arr)-1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         if arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None


def binSearch(arr, target, start, end) :
    if start > end :
        return None

    mid = (start + end)//2
    if arr[mid] == target :
        return mid # index를 return한다.
    if arr[mid] > target :
        return binSearch(arr, target, start, mid-1)
    elif arr[mid] < target :
        return binSearch(arr, target, mid+1, end)
        

arr = [1,2,3,4,5,6]
target = 2
n = len(arr)
print(binSearch(arr,target,0,n-1))
# print(b_search(arr,target))
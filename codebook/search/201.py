def binSearch(arr, target, start, end) :
    if start > end :
        close_ans = [start, end]
        return close_ans

    mid = (start + end)//2
    if arr[mid] == target :
        return mid # index를 return한다.
    if arr[mid] > target :
        return binSearch(arr, target, start, mid-1)
    elif arr[mid] < target :
        return binSearch(arr, target, mid+1, end)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_list = []
for i in range(max(arr)):
    sum_item = 0
    for item in arr :
        if item - i > 0 :
            sum_item += item-i
    sum_list.append(sum_item)

sum_list = sorted(sum_list)
result = len(sum_list) - (max(binSearch(sum_list, m, 0, n-1))+1)
print(result)

    
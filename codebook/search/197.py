
def binSearch(arr, target, start, end) :
    while start <= end :
        mid = (start + end)//2 
        if arr[mid] == target: return mid
        if arr[mid] > target: 
            end = mid - 1
        else :
            start = mid + 1
    return None

n=int(input())
item = list(map(int, input().split()))
item.sort()

m = int(input())
request = list(map(int, input().split()))

for i in range(m) :

    # 아래 줄 만 result = binSearh(...)으로 바꾸고
    # if result == None으로 해서 인스턴스로 검사하는게 더 가독성이 좋다.
    if binSearch(item, request[i], 0, n-1) == None :
        print('no', end=" ")
    else :
        print('yes', end=' ')


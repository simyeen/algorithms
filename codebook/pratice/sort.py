
data = [5,4,3,2,1]
n = len(data)

def insertion_sort():

    arr = [d for d in data]
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            break
    print('삽입 정렬', arr)

def selection_sort():
    arr = [d for d in data]
    
    for start in range(n-1):
        min_index = start
        for j in range(start+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[start], arr[min_index] = arr[min_index], arr[start]
    print('선택 정렬', arr)


def bubble_sort():
    arr = [d for d in data]
    for end in range(n-1, 0, -1):
        for j in range(0, end):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('버블 정렬', arr)




insertion_sort()
selection_sort()
bubble_sort()
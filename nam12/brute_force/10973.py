# n = int(input())
# a = list(map(int, input().split()))

# length = len(a) - 1

# k = -1
# for i in range(length):
#     if a[i] > a[i-1]:
#         k = i
# if k == -1:
#     print(-1)

# else:
#     m = -1
#     for j in range(k+1, length+1):
#         if a[k] > a[j]:
#             m = j

#     a[k], a[m] = a[m], a[k]

#     tmp = a[k+1:]
#     tmp.sort()
#     ans = a[:k+1] + tmp

# for num in ans:
#     print(num, end=" ")
# print()

# n = int(input())
# a = list(map(int, input().split()))

# length = len(a) - 1

# k = -1
# for i in range(length-1):
#     if a[i] > a[i+1]:
#         k = i
# if k == -1:
#     print(-1)

# else:
#     for j in range(k+1, length+1):
#         if a[k] > a[j]:
#             m = j

#     a[k], a[m] = a[m], a[k]
#     ans = []
#     tmp = a[k+1:]
#     tmp.sort()
#     ans = a[:k+1] + tmp

# for num in ans:
#     print(num, end=" ")
# print()

n = int(input())
lst = list(map(int, input().split()))

def prev_permutation(lst):
    if len(lst) == 1:
        return [-1]
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] <= lst[i - 1]:
            break
    if i == 1 and lst[0] < lst[1]:
        return [-1]
    # i - 1 인덱스에 위치한애가 바뀔 것이여
    for j in range(len(lst) - 1, 0 , -1):
        if lst[j] <= lst[i - 1]:
            break
    # j 인덱스하고 바뀔 것이여
    tmp = lst[j]
    lst[j] = lst[i - 1]
    lst[i - 1] = tmp

    lst = lst[:i] + sorted(lst[i:], reverse=True)
    return lst

print(' '.join(map(str, prev_permutation(lst))))

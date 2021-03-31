# N = int(input())
# before = list(map(int, input().split()))

# num = [i+1 for i in range(N+10)]
# check = [False for i in range(N+10)]
# arr = []
# find = False

# is_sorted = all(x > y for x, y in zip(before[:-1], before[1:]))
# if(is_sorted):
#     print(-1)
#     exit(0)


# def dfs(cnt):

#     global find
#     if(cnt == N):
#         if find:
#             print(*arr)
#             exit(0)

#         if arr == before:
#             find = True
#         return

#     for i in range(N):
#         if(check[i]):
#             continue

#         check[i] = True
#         arr.append(num[i])
#         dfs(cnt+1)
#         arr.pop()
#         check[i] = False


# dfs(0)


# N = int(input())
# a = list(map(int, input().split()))


# # 1. k의 최댓값 구하기.

# k = -1
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         k = i

# if k == -1:
#     print(-1)

# else:
#     for i in range(k+1, len(a)):
#         if a[k] < a[i]:
#             m = i
#     a[k], a[m] = a[m], a[k]

#     tmp = a[k+1:]
#     tmp.sort()
#     ans = a[:k+1] + tmp

# for num in ans:
#     print(num, end=' ')
# print()

# def next_per(a):
#     length = len(a) - 1

#     i = length
#     while i > 0 and a[i-1] >= a[i]:
#         i -= 1
#     if i <= 0:
#         return False

#     j = length
#     while a[i-1] >= a[j]:
#         j -= 1
#     a[i-1], a[j] = a[j], a[i-1]

#     j = length
#     while i < j:
#         a[i], a[j] = a[j], a[i]
#         i += 1
#         j -= 1

#     return True


# n = int(input())
# a = list(map(int, input().split()))

# if next_per(a):
#     print(*a)
# else:
#     print(-1)

import sys

n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

k = -1

for i in range(len(seq)-1):
    if seq[i] < seq[i+1]:
        k = i
if k == -1:
    print(-1)
else:
    for j in range(k+1, len(seq)):
        if seq[k] < seq[j]:
            m = j
    seq[k], seq[m] = seq[m], seq[k]

    tmp = seq[k+1:]
    tmp.sort()
    answer = seq[:k+1] + tmp

    for num in answer:
        print(num, end=' ')
    print()

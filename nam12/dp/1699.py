# n = int(input())

# d = [0 for _ in range(n+1)]


# d[1] = 1

# for i in range(2, n+1):

#     if i**2 < n:
#         d[i**2] = 1
#     min = 999999
#     for j in range(0, i//2):
#         if min > d[j] + d[i-j]:
#             min = d[j] + d[i-j]
#     d[i] = min

#     print(d[i])

import sys
n = int(sys.stdin.readline().rstrip())

d = [0 for _ in range(n+1)]

for i in range(1, n+1):
    d[i] = i
    for j in range(1, i):
        if j**2 > i:
            break
        elif d[i] > d[i - j**2] + 1:
            d[i] = d[i - j**2] + 1
print(d[n])

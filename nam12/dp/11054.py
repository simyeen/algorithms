# import sys

# n = int(sys.stdin.readline().rstrip())
# a = list(map(int, sys.stdin.readline().rstrip().split()))

# incre = [0 for i in range(1, n+1)]
# decre = [0 for i in range(1, n+1)]
# d = [0 for i in range(1, n+1)]

# for i in range(1, n+1):  # 0부터 끝까지

#     for j in range(1, i+1):  # i까지
#         max = 0

#         if a[i] < a[j] < max and decre[i] < decre[j]:
#             decre[i] = decre[j]
#             continue

#         if a[i] > a[j] and incre[i] < incre[j]:
#             incre[i] = incre[j]
#             max = a[i]
#             decre[i] = incre[i]

#     print("max", max)
#     if incre[i] == 0 or decre[i] == 0:
#         d[i] = 0

#     else:
#         d[i] = incre[i] + decre[i] + 1

# print(incre, decre)
# print(max(d))

# ==================================
import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

incre = [0 for i in range(n)]
decre = [0 for i in range(n)]
d = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and incre[i] < incre[j]:
            incre[i] = incre[j]
    incre[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and decre[i] < decre[j]:
            decre[i] = decre[j]
    decre[i] += 1

for i in range(n):
    d[i] = incre[i] + decre[i] - 1

print(max(d))

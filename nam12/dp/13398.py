# import sys

# n = int(sys.stdin.readline().rstrip())
# a = list(map(int, sys.stdin.readline().rstrip().split()))
# d = [[0]*2 for _ in range(n+10)]

# d[1][1] = a[1]
# d[1][0] = 0

# for i in range(1, n):
#     d[i][1] = a[i]
#     d[i][0] = max(d[i-1])

#     d[i] = max(d[i], d[i-1] + a[i])

# print(max(d))

import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

incre = [0]*n
decre = [0]*n
d = [0]*n

incre[0] = a[0]
decre[n-1] = a[n-1]

for i in range(1, n):
    incre[i] = max(incre[i-1]+a[i], a[i])

for i in range(n-2, -1, -1):
    decre[i] = max(decre[i+1]+a[i], a[i])

d[0], d[n-1] = a[0], a[n-1]
for i in range(1, n-1):
    d[i] = incre[i-1] + decre[i+1]

print(max(max(incre), max(d)))

import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0 for _ in range(n)]


d[0] = a[0]

# for i in range(1, n):

#     if d[i-1] + a[i] > d[i]:
#         d[i] = d[i-1] + a[i]

#     else:
#         d[i] = a[i]

for i in range(1, n):
    d[i] = a[i]

    if d[i] < (d[i-1] + a[i]):
        d[i] = d[i-1] + a[i]

print(max(d))

# ???? 왜 위에는 틀리고 밑에는 맞지... ?
# 왜냐면 위에 처럼 하면 d[i]는 default 값이 0이라서
# 원하는데로 안나올 수 있음!!

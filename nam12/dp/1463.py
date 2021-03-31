# import sys

# n = int(sys.stdin.readline().rstrip())
# MAX = 1000000

# d = [0 for _ in range(1, MAX+1)]

# d[1], d[2], d[3] = 0, 1, 1

# for i in range(4, n+1):
#     if i % 3 == 0 and i % 2 != 0:
#         d[i] = min(d[i//3], d[i-1]) + 1

#     elif i % 3 != 0 and i % 2 == 0:
#         d[i] = min(d[i//2], d[i-1]) + 1

#     elif i % 3 == 0 and i % 2 == 0:
#         d[i] = min(d[i//3], d[i//2], d[i-1]) + 1

#     else:
#         d[i] = d[i-1] + 1
# for i in range(1, n+1):

#     print(i, d[i])


# ========================================

# import sys

# n = int(sys.stdin.readline().rstrip())

# d = [0] * (n+1)  # d = [0 for _ in range(1, n+1)]

# d[1], d[2], d[3] = 0, 1, 1

# for i in range(4, n+1):

#     d[i] = d[i-1] + 1

#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)

# print(d[n])

# 3부터 검사가 아니라 1부터 함.

# ==========================================


import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+1)  # d = [0 for _ in range(1, n+1)]

d[1] = 0

for i in range(2, n+1):

    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

for i in range(1, n+1):

    print(i, d[i])

# 초기화를 d[1]만 해주니깐 됫음 왜지???

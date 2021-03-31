
# n = int(input())
# w = [0]
# for i in range(n):
#     w.append(int(input()))
# dp = [0]
# dp.append(w[1])
# if n > 1:
#     dp.append(w[1] + w[2])
# for i in range(3, n + 1):
#     dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
# print(dp[n])

# 런타임 에러
# import sys

# n = int(sys.stdin.readline())
# numbers = [0] * (n)
# D = [0] * (n)
# for i in range(n):
#     numbers[i] = int(sys.stdin.readline())
# D[0] = numbers[0]
# D[1] = numbers[0] + numbers[1]

# for i in range(2, n):
#     a = D[i-1]
#     b = D[i-2] + numbers[i]
#     c = D[i-3] + numbers[i] + numbers[i-1]
#     D[i] = max(a, b, c)

# print(D[n-1])


# 틀렸습니다 -> index 하나씩 앞으로 해줌.., 런타임 에러
import sys

n = int(sys.stdin.readline())
numbers = [0] * (n+1)
D = [0] * (n+1)
for i in range(1, n+1):
    numbers[i] = int(sys.stdin.readline())
D[0] = 0
D[1] = numbers[1]

if n > 1:
    D[2] = numbers[1] + numbers[2] # 1이 들어오는 경우 때문에 런타임에러
# i = 3
# 1 2 3
# o/x o/x x = d[i-1]
# o/x x o = d[i-2] + w[i]
# x o o = w[i-1] + w[i] + d[i-3]
for i in range(3, n+1):
    a = D[i-1]
    b = D[i-2] + numbers[i]
    c = D[i-3] + numbers[i] + numbers[i-1]
    D[i] = max(a, b, c)

print(D[n])

# 런타임 에러
# import sys

# n = int(sys.stdin.readline())
# numbers = [0] * n
# D = [0] * (n+1)
# for i in range(n): 
#     numbers[i] = int(sys.stdin.readline())
# D[0] = 0
# D[1] = numbers[0]
# D[2] = numbers[0] + numbers[1]

# for i in range(3, n+1):
#     a = D[i-1]
#     b = D[i-2] + numbers[i-1]
#     c = D[i-3] + numbers[i-2] + numbers[i-1]
#     D[i] = max(a, b, c)

# print(D[n])
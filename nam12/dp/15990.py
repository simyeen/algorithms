# import sys

# t = int(sys.stdin.readline().rstrip())


# for _ in range(t):
#     n = int(sys.stdin.readline().rstrip())
#     d = [[0]*3 for i in range(1, n+1)]

#     d[1][0], d[1][1], d[1][2] = 1, 0, 0
#     d[2][0], d[2][1], d[2][2] = 0, 1, 0
#     d[3][0], d[3][1], d[3][2] = 1, 1, 1 #초기화

#     for i in range(4, n+1): # 메모가 안돼 있음.
#         d[i][0] = (d[i-1][1] + d[i-1][2]) % 1000000009
#         d[i][1] = (d[i-2][0] + d[i-2][2]) % 1000000009
#         d[i][2] = (d[i-3][0] + d[i-3][1]) % 1000000009 #메모리초과

#     ans = 0
#     for i in range(3):
#         ans += d[n][i]

#     print(ans % 1000000009)

# 이렇게 짜면 O(n^2)이라서 시간초과가 뜬다.
# 비효율 처럼 보이지만 먼저 dp값들을 다 구해놓고
# 원하는 값만 출력하게 하면 O(n)이므로 아래처럼 해야한다.

import sys

MAX = 100000
MOD = 1000000009

d = [[0]*4 for i in range(MAX+10)]
d[1] = [0, 1, 0, 0]
d[2] = [0, 0, 1, 0]
d[3] = [0, 1, 1, 1]

for i in range(4, MAX+10):
    d[i][1] = (d[i-1][2] + d[i-1][3]) % MOD
    d[i][2] = (d[i-2][1] + d[i-2][3]) % MOD
    d[i][3] = (d[i-3][2] + d[i-3][1]) % MOD

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(sum(d[n]) % MOD)

# O(n) => 출력 좀 잘 고려해주기.

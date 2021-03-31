import sys

t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    d = [0] * (n+10)

    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])

# d[0] * (n+1) 까지 돌리면 런타임 에러이므로 주의

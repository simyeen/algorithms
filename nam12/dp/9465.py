import sys

t = int(sys.stdin.readline().rstrip())


for i in range(t):

    n = int(sys.stdin.readline().rstrip())
    d, p = [[0]*(n+1) for _ in range(2)], [[0]*(n+1) for _ in range(2)]

    for i in range(2):
        p[i] = list(map(int, sys.stdin.readline().rstrip().split()))
        p[i].insert(0, 0)
    d[0][1] = p[0][1]
    d[1][1] = p[1][1]

    for j in range(2, n+1):

        d[0][j] = p[0][j] + d[1][j-1]
        d[1][j] = p[1][j] + d[0][j-1]

        if p[1][j] > p[0][j] + p[1][j-1]:
            d[0][j] = p[1][j] + max(d[0][j-2], d[1][j-2])

        if p[0][j] > p[1][j] + p[1][j-1]:
            d[1][j] = p[0][j] + max(d[0][j-2], d[1][j-2])
    print(max(d[0][n], d[1][n]))

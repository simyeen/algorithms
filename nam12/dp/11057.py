import sys

n = int(sys.stdin.readline().rstrip())

d = [[0]*10 for _ in range(n+1)]
d[1] = [1]*10

for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += (d[i-1][k]) % 10007

print(sum(d[n]) % 10007)

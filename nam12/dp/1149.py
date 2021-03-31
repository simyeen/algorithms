import sys

n = int(sys.stdin.readline().rstrip())

p = [[0]*3 for _ in range(n+1)]
d = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    p[i] = list(map(int, (sys.stdin.readline().rstrip().split())))

d[1] = p[1]


for i in range(2, n+1):
    d[i][0] = p[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = p[i][1] + min(d[i-1][2], d[i-1][0])
    d[i][2] = p[i][2] + min(d[i-1][0], d[i-1][1])
print(min(d[n]))

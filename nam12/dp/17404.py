import sys

n = int(sys.stdin.readline().rstrip())

p = [[0]*3 for _ in range(n+1)]
d = [[0]*3 for _ in range(n+1)]
start = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    p[i] = list(map(int, (sys.stdin.readline().rstrip().split())))

d[1] = p[1]
start[1] = [0, 1, 2]

for i in range(2, n+1):

    if d[i-1][1] > d[i-1][2]:
        d[i][0] += p[i][0] + d[i-1][2]
        start[i][0] = start[i-1][2]
    else:
        d[i][0] += p[i][0] + d[i-1][1]
        start[i][0] = start[i-1][1]

    if d[i-1][0] > d[i-1][2]:
        d[i][1] += p[i][1] + d[i-1][2]
        start[i][1] = start[i-1][2]
    else:
        d[i][1] += p[i][1] + d[i-1][0]
        start[i][1] = start[i-1][0]

    if d[i-1][1] > d[i-1][0]:
        d[i][2] += p[i][2] + d[i-1][0]
        start[i][2] = start[i-1][0]
    else:
        d[i][2] += p[i][2] + d[i-1][1]
        start[i][2] = start[i-1][1]

print(p)
print(d)
print(start)
ans = []

for i in range(3):
    if start[n][i] != i:
        ans.append(d[n][i])
print(ans)
print(min(ans))

# 틀린 이유 :

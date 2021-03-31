import sys

n = int(sys.stdin.readline().rstrip())

p = list(map(int, sys.stdin.readline().rstrip().split()))
p.insert(0, 0)

d = [0 for _ in range(n+10)]

d[0], d[1] = 0, p[1]

for i in range(2, n+1):

    d[i] = 99999

    for j in range(1, i+1):
        d[i] = min(d[i-j]+p[j], d[i])

print(d[n])

import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+1)

d[1], d[2] = 1, 3

for i in range(3, n+1):
    d[i] = d[i-1] + 2*d[i-2]

print(d[n] % 10007)

# ???????? -,-

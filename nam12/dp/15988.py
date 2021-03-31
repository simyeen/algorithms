import sys

MAX = 1000000
MOD = 1000000009

d = [0 for i in range(MAX+10)]
d[0] = 1
d[1] = 1
d[2] = 2

for i in range(3, MAX+10):
    d[i] = d[i-1] % MOD + d[i-2] % MOD + d[i-3] % MOD

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(d[n] % MOD)

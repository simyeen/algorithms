import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0 for i in range(n+5)]

for i in range(n):
    d[i] += a[i]
    temp = 0
    for j in range(i):
        if temp < a[j] < a[i]:
            d[i] += a[j]
            temp = a[j]

print(d)
print(max(d))

# 답은 맞는데 틀린거 보니까 dp로 안풀어서 틀린 것 같음.

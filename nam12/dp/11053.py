import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0 for i in range(n)]

for i in range(n):  # 0부터 끝까지
    for j in range(i):  # i까지
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))

# O(n^2)
# 이 방법이 최선인가 ?? stack써서 index저장하듯이하면...?

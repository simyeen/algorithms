import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0 for i in range(n)]
p = [[0]*0 for i in range(n)]

for i in range(n):  # 0부터 끝까지
    for j in range(i):  # i까지
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
            p[i].append(j)
    d[i] += 1
    p[i].append(i)

print(max(d))

leng = 0
temp = 0
for i in range(n):
    if leng < len(p[i]):
        leng = len(p[i])
        temp = i

for i in p[temp]:
    print(a[i], end=" ")
print(p)
# 경로 추적할 때 다잌스트라 하듯이 해도 될듯

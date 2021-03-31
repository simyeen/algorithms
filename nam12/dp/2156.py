import sys

n = int(sys.stdin.readline().rstrip())
a = [0]
d = [0]

for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

d.append(a[1])
# d.append(a[1]+a[2])
if n >= 2:  # 초항을 2까지 줘야 돼서 이렇게 했음. n = 1이면 a[2]가 없으니깐..
    d.append(a[1] + a[2])

for i in range(3, n+1):
    d.append(max(a[i] + a[i-1] + d[i-3], a[i] + d[i-2], d[i-1]))
print(d[n])

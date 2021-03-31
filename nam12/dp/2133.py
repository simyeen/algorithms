n = int(input())

if n % 2 != 0:
    print(0)
    exit()

d = [0 for _ in range(n+1)]
d[2] = 3

for i in range(4, n+1, 2):
    d[i] = d[i-2] * d[2] + 2  # 기존에 2개 타일 붙이기.
    for j in range(4, i, 2):
        d[i] += d[i-j]*2     # 처음 시작이 타일 4개, 6개
print(d[n])

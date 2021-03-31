n = int(input())

a = [[0]*(i+1) for i in range(n+5)]
d = [[0]*(i+1) for i in range(n+5)]

for i in range(1, n+1):
    a[i] = list(map(int, input().split()))
    a[i].insert(0, 0)
d[1][1] = a[1][1]
d[2][1] = a[2][1] + d[1][1]
d[2][2] = a[2][2] + d[1][1]

for i in range(3, n+1):
    for j in range(1, i+1):
        if j == 1:
            d[i][j] = a[i][j] + d[i-1][1]  # 제일 왼쪽
            continue
        elif j == i:
            d[i][j] = a[i][j] + d[i-1][j-1]  # 제일 오른쪽
            break
        else:
            d[i][j] = a[i][j] + max(d[i-1][j-1], d[i-1][j])

print(max(d[n]))
#index 잘보기!
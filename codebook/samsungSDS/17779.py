n = int(input())
data = [[0]*(n+1)]
for _ in range(n):
    data.append([0] + list(map(int, input().split())))
total = 0
for d in data: total += sum(d)

def calculrate(x, y, d1, d2):
    zone = [0]*4
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(d1+1):
        arr[x + i][y - i] = 5
        arr[x + d2 + i][y + d2 - i] = 5
    for i in range(d2+1):
        arr[x + i][y + i] = 5
        arr[x + d1 + i][y - d1 + i] = 5

    # 1번 zone
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if arr[r][c] == 5: break
            arr[r][c] = 1
            zone[0] += data[r][c]
    # 2번 zone
    for r in range(1, x+d2+1):
        for c in range(n, y, -1):
            if arr[r][c] == 5: break
            arr[r][c] = 2
            zone[1] += data[r][c]
    # 3번 zone
    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if arr[r][c] == 5: break
            arr[r][c] = 3
            zone[2] += data[r][c]
    # 4번 zone
    for r in range(x+d2+1, n+1):
        for c in range(n, y-d1+d2-1,-1):
            if arr[r][c] == 5: break
            arr[r][c] = 4
            zone[3] += data[r][c]

    five_zone = total - sum(zone)
    zone += [five_zone]
    return max(zone) - min(zone)

ans = 1e9
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue
                ans = min(ans, calculrate(x, y, d1, d2))
print(ans)



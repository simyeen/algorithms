from collections import deque

r, c, t = map(int, input().split())

data = []
for _ in range(r): data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

machine, dusts = [], []
for i in range(r):
    for j in range(c):
        if data[i][j] == -1: machine.append((i, j))
        if data[i][j] > 0: dusts.append((i, j))

x1, y1 = machine[0]
x2, y2 = machine[1]


def spread():
    spread_data = [[0 for _ in range(c)] for _ in range(r)]
    spread_data[x1][y1], spread_data[x2][y2] = -1, -1
    spread_list = []

    while dusts:
        x, y = dusts.pop()
        tmp = [(x, y)]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in machine: continue
            if 0 <= nx < r and 0 <= ny < c:
                tmp.append((nx, ny))
        spread_list.append(tmp)

    for dust in spread_list:
        x, y = dust[0]
        mini_dust = int(data[x][y] / 5)
        if mini_dust == 0:
            spread_data[x][y] += data[x][y]
            continue
        for nx, ny in dust[1:]:
            spread_data[nx][ny] += mini_dust
        rest_dust = data[x][y] - (mini_dust * (len(dust) - 1))
        spread_data[x][y] += rest_dust

    return spread_data


def cycle_air():
    # 위쪽 순환 4번의 과정
    for row in range(x1 - 1, -1, -1):  # 역순으로 땡기지는 식
        if row + 1 == x1: continue
        data[row + 1][0] = data[row][0]
    for col in range(1, c):
        data[0][col - 1] = data[0][col]
    for row in range(1, x1 + 1):
        data[row - 1][c - 1] = data[row][c - 1]
    for col in range(c - 2, 0, -1):
        data[x1][col + 1] = data[x1][col]
    data[x1][y1 + 1] = 0

    for row in range(x2 + 2, r):
        data[row - 1][0] = data[row][0]
    for col in range(1, c):
        data[r - 1][col - 1] = data[r - 1][col]
    for row in range(r - 2, x2 - 1, -1):
        data[row + 1][c - 1] = data[row][c - 1]
    for col in range(c - 2, 0, -1):
        data[x2][col + 1] = data[x2][col]
    data[x2][y2 + 1] = 0

    for i in range(r):
        for j in range(c):
            if data[i][j] > 0: dusts.append((i, j))


for _ in range(t):
    data = spread()
    cycle_air()

ans = 0
for i in range(r):
    for j in range(c):
        if data[i][j] > 0: ans += data[i][j]
print(ans)
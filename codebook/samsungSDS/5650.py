
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 0. 항상 nx, ny을 가지고 판단한다.
# 1. 종료 조건 : 원래 출발 지점 혹은 블랙홀을 만난다.
# 2. 벽을 만난다 => 이동하지 않고, 반대 방향을 가진다.
# 3. block을 만난다 => block의 종료에 따라서 다른 방향을 return받고 이동한다.
# 4. 0을 만난다. 그냥 이동한다.
# 5. 웜홀을 만난다. 새로운 곳으로 이동한다.

def chage_d(d, kind):
    direction = [
        (2, 3, 1, 0),
        (1, 3, 0, 2),
        (3, 2, 0, 1),
        (2, 0, 3, 1),
        (2, 3, 0, 1)
    ]
    return direction[kind][d]

def simulation(x, y, d, data, warmholes):
    score = 0
    start = [x, y]
    while True:
        nx, ny = x+dx[d], y+dy[d]
        if [nx, ny] == start or data[nx][ny] == -1:
            break

        if 6 <= data[nx][ny] <= 10:
            [x1, y1] = warmholes[data[nx][ny]][0]
            [x2, y2] = warmholes[data[nx][ny]][1]
            if [nx, ny] == [x1, y1]:
                x, y = x2, y2
            else:
                x, y = x1, y1

        elif 1 <= data[nx][ny] <= 5:
            d = chage_d(d, data[nx][ny]-1)
            x, y = nx, ny
            score += 1

        elif data[nx][ny] == 0:
            x, y = nx, ny

    return score

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = [[5] * (n+2)]
    for _ in range(n):
        tmp = list(map(int, input().split()))
        tmp = [5] + tmp + [5]
        data.append(tmp)
    data = data + [[5] * (n+2)]

    warmholes = [[] for _ in range(11)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if 6 <= data[i][j] <= 10:
                warmholes[data[i][j]].append([i, j])

    ans = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if data[i][j] == 0:
                for d in range(4):
                    ans.append(simulation(i, j, d, data, warmholes))
    print(max(ans))


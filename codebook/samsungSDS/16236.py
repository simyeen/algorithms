from collections import deque

n = int(input())
data = []
for _ in range(n): data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_data(shark, data):

    arr = [d[:] for d in data]
    x, y, size = shark
    q = deque()
    q.append([x, y, 0])
    arr[x][y] = -1
    fishes = []
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0<=nx<n and 0<=ny<n): continue
            if arr[nx][ny] > size or arr[nx][ny] == -1: continue
            # 이동하기
            if arr[nx][ny] != 0 and arr[nx][ny] < size:
                fishes.append([nx, ny, dist+1])
            q.append([nx, ny, dist+1])
            arr[nx][ny] = -1

    return fishes

shark = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark = [i, j, 2]
time = 0
cnt = 0
while True:
    find_fish = find_data(shark, data)
    if len(find_fish) == 0: break
    if len(find_fish) >= 2:
        find_fish.sort(key=lambda x: (x[2], x[0], x[1]))

    # 먹고 이동한다.
    x, y, dist = find_fish[0]
    s_x, s_y, size = shark

    data[s_x][s_y] = 0
    data[x][y] = 9
    time += find_fish[0][2]
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0

    shark = [x, y, size]

print(time)
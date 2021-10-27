from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y, arr):
    q = deque()
    q.append((x, y))

    block = arr[x][y]
    blocks = [[x, y, block]]
    rainbow_blocks = []

    if block > 0:
        flag = True
    elif block == 0:
        flag = False
        rainbow_blocks.append([x, y])

    arr[x][y] = -2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n): continue
            if arr[nx][ny] < 0: continue
            if arr[nx][ny] == 0 or arr[nx][ny] == block:
                if arr[nx][ny] > 0: flag = True
                if arr[nx][ny] == 0: rainbow_blocks.append([nx, ny])
                blocks.append([nx, ny, arr[nx][ny]])
                q.append((nx, ny))
                arr[nx][ny] = -2

    for x, y in rainbow_blocks: arr[x][y] = 0

    if len(blocks) >= 2 and flag:
        blocks.sort(key=lambda x : (-x[2], x[0], x[1]))
        return blocks
    return []

def find_largest_index(block_group):
    sorting_list = [[i] for i in range(len(block_group))]

    for i in range(len(block_group)):
        group = block_group[i]
        sorting_list[i].append(len(group))
        zero_cnt = 0
        for x, y, value in group:
            if value == 0: zero_cnt += 1
        sorting_list[i].append(zero_cnt)
        if group[0][2] != 0:
            sorting_list[i].append(group[0][0])
            sorting_list[i].append(group[0][1])
        else :
            sorting_list[i].append(-1)
            sorting_list[i].append(-1)

    sorted_list = sorted(sorting_list, key=lambda x : (-x[1], -x[2], -x[3], -x[4]))
    return sorted_list[0][0]

def new_data(largest_group, data):
    global ans
    ans += len(largest_group)**2
    for x, y, value in largest_group:
        data[x][y] = -2


def grivated_data():
    global data

    n, m = len(data), len(data[0])
    for j in range(m):
        ind = n-1
        for i in range(n-1, -1, -1):
            if data[i][j] == -2:
                continue
            if data[i][j] == -1 or ind == i:
                ind = i-1
                continue
            data[ind][j] = data[i][j]
            data[i][j] = -2
            ind -= 1

def rotate():
    global data
    tmp = [a[:] for a in data]
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(3):
        for r in range(n):
            for c in range(n):
                ret[r][c] = tmp[n-c-1][r]
        tmp = [re[:] for re in ret]

    data = ret

n, m = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))

ans = 0
arr = [d[:] for d in data]
while True:
    block_group = []
    for x in range(n):
        for y in range(n):
            if arr[x][y] < 0: continue
            group = bfs(x, y, arr)
            if not group: continue
            block_group.append(group)

    if len(block_group) == 0:
        break

    index = find_largest_index(block_group)
    largest_group = block_group[index]

    new_data(largest_group, data)
    grivated_data()
    rotate()
    grivated_data()

    arr = [d[:] for d in data]

print(ans)




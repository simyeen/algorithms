from collections import deque

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))

candidates, virus = [], []
for i in range(n):
    for j in range(m):
        if data[i][j] == 2: virus.append((i, j))
        elif data[i][j] == 0: candidates.append((i, j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,arr):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<m) or arr[nx][ny] == 1: continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))

def check_cnt(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: cnt+=1
    return cnt

ans = 0
for combination in combinations(candidates, 3):
    new_data = [d[:] for d in data]
    for i, j in combination:
        new_data[i][j] = 1
    for x, y in virus:
        bfs(x, y, new_data)

    ans = max(ans, check_cnt(new_data))

print(ans)
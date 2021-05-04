from collections import deque

n, k = map(int, input().split())

data = []
q = [deque() for i in range(k+1)]

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        target = data[i][j]
        if target != 0:
            q[target].append((i, j))

s, r, c = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(cur, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = cur
                q[cur].append((nx, ny))

for _ in range(s):
    for i in range(1, k+1):
        if q[i]:
            x, y = q[i].popleft()
            bfs(i, x, y)

print(data)
print(data[r-1][c-1])

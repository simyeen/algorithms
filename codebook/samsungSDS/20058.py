from collections import deque

n, q = map(int, input().split())

data = []
for _ in range(2**n):
    data.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))
for i in range(len(cmds)):
    cmds[i] %= 10

def rotate(x, y, data, L):
    ret = [[0 for _ in range(2**L)] for _ in range(2**L)]
    for r in range(2**L):
        for c in range(2**L):
            ret[r][c] = data[x + 2**L-c-1][y + r]

    for r in range(2**L):
        for c in range(2**L):
            data[x+r][y+c] = ret[r][c]


def bfs(x, y, data):
    ice = 1
    q = deque()
    q.append((x, y))
    data[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<2**n and 0<=ny<2**n) or data[nx][ny] == 0: continue
            q.append((nx, ny))
            data[nx][ny] = 0
            ice += 1

    return ice

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for L in cmds:
    for x in range(0, 2**n, 2**L):
        for y in range(0, 2**n, 2**L):
            rotate(x, y, data, L)

    remove_ice = []
    for x in range(2**n):
        for y in range(2**n):
            if data[x][y] == 0: continue
            cnt = 0

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if not(0<=nx<2**n and 0<=ny<2**n) or data[nx][ny] == 0: continue
                cnt += 1
            if cnt < 3: remove_ice.append((x, y))

    for x, y in remove_ice:
        data[x][y] -= 1

ans = 0
for x in range(2**n):
    for y in range(2**n):
        ans += data[x][y]

large_ice = -1e9
for x in range(2**n):
    for y in range(2**n):
        if data[x][y] == 0: continue
        large_ice = max(large_ice, bfs(x, y, data))

print(ans)
if ans == 0: print(0)
else: print(large_ice)


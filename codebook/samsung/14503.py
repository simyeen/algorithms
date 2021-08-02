import copy
from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = 0

data = []
for _ in range(n): data.append(list(map(int, input().split())))
cleared_data = copy.deepcopy(data)

def rotate(d):
    return 3 if d == 0 else d-1

def bfs(x,y):
    global d
    q = deque()
    q.append((x,y))
    cleared_data[x][y] = 2 # 청소한 곳은 2로 표시

    while q:
        x, y = q.pop()
        check_cnt = 0 
        for _ in range(4):
            d = rotate(d)
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1 or cleared_data[nx][ny] == 2 : # 벽이거나 청소가 되어있는 곳
                    check_cnt += 1
                    continue
                if data[nx][ny] == 0 and cleared_data[nx][ny] == 0 : # 청소가 안되있는 곳.
                    cleared_data[nx][ny] = 2
                    q.append((nx,ny)) # 이동하기
                    break
        if check_cnt == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if data[nx][ny] == 0 : 
                q.append((nx,ny))
            else : break
        
bfs(x,y)

ans = 0
for i in range(n):
    for j in range(m):
        if cleared_data[i][j] == 2: ans +=1
print(ans)



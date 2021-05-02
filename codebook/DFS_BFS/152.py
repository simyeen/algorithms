from collections import deque

row, col = map(int, input().split())

arr = []
for _ in range (row) :
    arr.append(list(map(int, input())))

drow = [-1, 0, 1, 0] #반시계 방향 up left down right 순이다.
dcol = [0, -1, 0, 1]

dist = 1

def bfs(r,c):
    queue = deque()
    queue.append((r,c))

    while queue :
        r, c = queue.popleft()
        for i in range(4) :
            nr = r + drow[i]
            nc = c + dcol[i]
            if nr < 0 or nc < 0 or nr >= row or nc >= col :
                continue
            if arr[nr][nc] == 0 :
                continue
            if arr[nr][nc] == 1 :
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr,nc))
    return arr[row-1][col-1]

print(bfs(0,0))



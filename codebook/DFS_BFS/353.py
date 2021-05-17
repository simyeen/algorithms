from collections import deque

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
graph = [[0]* n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
num = 1

def reset(num, avg):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                data[i][j] = avg

def bfs(x, y, cnt):
    global result
    global num 
    
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        graph[x][y] = num

        for i in range(4):     
            nx = x + dx[i] 
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
    
            if l <= abs(data[x][y] - data[nx][ny]) <= r :
                graph[nx][ny] = num
                avg = ((data[x][y] * cnt) + data[nx][ny] ) // (cnt+1)
                cnt += 1
                reset(num, avg)
                q.append((nx, ny))
        print(x,y,data, graph)
    num += 1

result = 0
for i in range(n):
    for j in range(n):
        bfs(i, j, 1)

print(data)
print(graph)
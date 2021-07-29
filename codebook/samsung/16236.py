from collections import deque
import copy

n = int(input())

data = []
for _ in range(n): data.append(list(map(int, input().split())))

x, y = 0,0
for i in range(n):
    for j in range(n): 
        if data[i][j] == 9 : 
            x,y = i,j
            data[i][j] = 0
            
dx = [-1,0,1,0]
dy = [0,1,0,-1]

size, cnt, time = 2, 0, 0


while True:      
    graph = copy.deepcopy(data)
    q = deque()
    q.append((x,y,0))
    graph[x][y] = -1
    tmp = []

    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            target = graph[nx][ny] 
            if target == 0 or target == size : # 이동할 수 있음.
                q.append((nx,ny,dist+1))
                graph[nx][ny] = -1
            if 0 < target and target < size: # 먹을 수 있음.
                tmp.append((nx,ny,dist+1))
    tmp.sort(key=lambda x : (x[2],x[0],x[1]))
    if len(tmp) == 0 : break # 먹을 수 없을 때. 종료
    x, y = tmp[0][0], tmp[0][1] # 먹을 수 있을 때
    data[x][y] = 0
    cnt += 1 
    time += tmp[0][2]
    if cnt == size : 
        size += 1
        cnt = 0
print(time)


# 더이상 먹을 물고기가 없다는 것 과 이동 불가라는 2가지 조건.
# bfs해서 tmp를 담을때 tmp가 비었으면 return 해버리게
# x,y의 위치에서 bfs로 먹을수 있는 node들을 쫙 다 구한다
# tmp에 1. 거리순으로, row, col순으로 정렬
# tmp[0]빼서 그 x,y칸 안에 
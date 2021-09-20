# 원판 돌리기

from collections import deque

n, m, t = map(int, input().split())
data = []
for _ in range(n) : data.append(list(map(int, input().split())))
cmds = []
for _ in range(t) : cmds.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def rotate(cmd, arr):
    x, d, k = cmd
    circle_index = []
    for i in range(x,n+1,x): circle_index.append(i-1)
    for index in circle_index:
        for _ in range(k):
            if d == 0 : arr[index].insert(0,(arr[index].pop()))
            elif d == 1 : arr[index].append(arr[index].pop(0))

def bfs(x,y,arr):
    
    global n, m
    if arr[x][y] == -1 : return 0

    q = deque()
    q.append((x,y,arr[x][y]))
    
    new_arr = [a[:] for a in arr]
    remove_list = []
    while q:
        x, y, target = q.pop()
        for i in range(4):
            if x == 0 and i == 0 : continue
            if x == n-1 and i == 2 : continue
            nx, ny = (x+dx[i])%n, (y+dy[i])%m
            if not(0<=nx<n and 0<=ny<m) or new_arr[nx][ny] == -1: continue
            if target == new_arr[nx][ny] :
                remove_list.append((x,y))
                remove_list.append((nx,ny))
                q.append((nx,ny,new_arr[nx][ny]))
                new_arr[x][y], new_arr[nx][ny] = -1, -1

    if not remove_list : return 0
    else :
        for x,y in remove_list: arr[x][y] = -1
        return 1
            
arr = [d[:] for d in data]
for cmd in cmds:    
    rotate(cmd, arr)

    cnt = 0
    for i in range(n):
        for j in range(m): cnt +=  bfs(i,j,arr)

    if cnt > 0 : continue # 단, 한번이라도 cnt가 세짐.

    sum_value, cnt = 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1 : 
                sum_value += arr[i][j]
                cnt += 1
    
    if cnt == 0 : continue
    avg = float(sum_value/cnt)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1: continue
            if float(arr[i][j]) > avg : arr[i][j] -=1
            elif float(arr[i][j]) < avg : arr[i][j]+= 1

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != -1 : ans += arr[i][j]
print(ans)
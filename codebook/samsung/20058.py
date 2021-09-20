# 마법사 상어와 파이어스톰
from collections import deque

n, q = map(int, input().split())
data = []
for _ in range(2**n): data.append(list(map(int, input().split())))
cmds = list(map(int, input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def rotate_90(m): 
    N = len(m) 
    ret = [[0] * N for _ in range(N)] 
    for r in range(N): 
        for c in range(N): 
            ret[c][N-1-r] = m[r][c] 
    return ret

def firestorm(start_list,e):
    global n
    for start in start_list:
        x,y = start
        arr = [[0 for _ in range(e)] for _ in range(e)]
        for i in range(x,x+e):
            for j in range(y,y+e):
                arr[i-x][j-y] = data[i][j]
        tmp = rotate_90(arr)
        for i in range(x, x+e):
            for j in range(y,y+e):
                data[i][j] = tmp[i-x][j-y]

    minus_list = []
    for i in range(2**n):
        for j in range(2**n):
            x, y = i, j
            if data[x][y] == 0 : continue
            cnt = 0
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if not (0<=nx<2**n and 0<=ny<2**n) : continue
                if data[nx][ny] == 0: continue
                cnt += 1
            if data[x][y] > 0 and cnt < 3 : minus_list.append((x,y))
    
    if len(minus_list) >= 1:
        for x, y in minus_list: data[x][y] -= 1

for L in cmds:
    e = 2**L    
    start_list =[]
    for i in range(0,2**n,e):
        for j in range(0,2**n,e):
            start_list.append((i,j))
    firestorm(start_list,e)

sum_value, cnt_list = 0, []
for d in data : sum_value += sum(d)
for i in range(2**n):
    for j in range(2**n):
        x, y = i, j
        if data[x][y] == 0 : continue        
        q = deque()
        q.append((x,y))
        cnt = 0
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if not (0<=nx<2**n and 0<=ny<2**n) : continue
                if data[nx][ny] == 0: continue
                data[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
        cnt_list.append(cnt)

print(sum_value)
if len(cnt_list) == 0 : print(0)
else : print(max(cnt_list))
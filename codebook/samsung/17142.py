
from itertools import combinations
from collections import deque
import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n, m = map(int, input().split())
data = []
for _ in range(n) : data.append(list(map(int, input().split())))

check = 0
blocks, virus = [], []
dist_data = [[' ' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 2 : 
            virus.append((i,j))
            dist_data[i][j] = '*'
        elif data[i][j] == 1 : 
            blocks.append((i,j))
            dist_data[i][j] = '-'
        else : check += 1
check += len(virus)

ans = []
combination = list(combinations(virus, m))
for combi in combination:
    q = deque()
    tmp_data = copy.deepcopy(dist_data)

    for virus in combi : 
        x, y = virus
        dist = 0
        q.append((x,y,0))
        tmp_data[x][y] = 0 # 활성 바이러스들

    cnt, max_value = 0, -1e9
    while q:
        x, y, dist = q.popleft()
        cnt += 1

        if tmp_data[x][y] != '+' : # 비활성 바이러스를 만나면은?
            tmp_data[x][y] = str(dist)
            max_value = max(dist, max_value)
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<n) : continue
            if tmp_data[nx][ny] == '-' : continue

            if tmp_data[nx][ny] == '*' : # 비활성 바이러스를 만났을 때
                tmp_data[nx][ny] = '+' # 활성으로 변해버린 바이러스
                q.append((nx,ny,dist+1))
                continue
            if tmp_data[nx][ny] == ' ':
                tmp_data[nx][ny] = str(dist+1)
                q.append((nx,ny,dist+1))
    if check == cnt : ans.append(max_value)
    else : ans.append(-1)

print(min(ans))



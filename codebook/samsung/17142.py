# 바이러스는 비활성 / 활성 상태
# 활성 상태 바이러스는 상하좌우로 모든 빈칸으로 동시 복제 => 1초
# M개의 바이러스를 활성 상태로 변경

# 활성 바이러스는 비활성을 활성시킨다.

# 바이러스 중에 누구누구를 할지 뽑자 

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

data = []
for _ in range(n): data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

virus_list = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2: virus_list.append((i,j))

combination = list(combinations(virus_list,m))

ans = []
for combi in combination:

    lab = copy.deepcopy(data) 
    q = deque()
    for c in combi : 
        x, y = c
        dist = 0
        q.append((x, y, dist))
        lab[x][y] = '시작'

    while q :
        x, y, dist = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0<=nx<n and 0<=ny<n) : continue
            if lab[nx][ny] == 0 : 
                q.append((nx,ny,dist+1))
                lab[nx][ny] = dist + 1
                
    for i in lab : print(i)
    print()

        


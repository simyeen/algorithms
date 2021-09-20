# 구슬 탈출 2

# 목표 : 빨간 구슬을 구멍으로 꺼내자
# 파란구슬이 빠지면 실패, 동시에 빠져도 실패.

from collections import deque

n, m = map(int, input().split())
dx = [-1,0,0,1]
dy = [0,-1,1,0]

data = []
for _ in range(n): 
    tmp = input()
    data.append([st for st in tmp])

for i in range(n):
    for j in range(m):
        if data[i][j] == 'R': x1, y1 = i, j
        if data[i][j] == 'B': x2, y2 = i, j

q = deque()
q.append((x1,y1,x2,y2,0))

ans = []
while q:
    x,y,x2,y2,cnt = q.popleft()
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not(0<=nx<n and 0<=ny<m) : continue
        if data[nx][ny] == '#' : continue
        if data[nx][ny] == 'B' : 
        
        
# 1. 구슬을 이리저리 굴린다.
# 2. R이 0이 도달하면 ans에 cnt를 추가해준다.
# 3. q에는 R, B 둘다 존재하는데 R을 움직이고, 그 다음에 B를 움직인다.
# 4. R이 움직이다가 B에 닿으면 예외처리 해주기.
# 5. 벽에 닿으면 append하고 cnt증가.
# 6. cnt 10이상은 continue



print (-1)

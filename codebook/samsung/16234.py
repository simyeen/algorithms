from collections import deque
import copy

N, L, R = map(int, input().split())

data = []
for _ in range(N): data.append(list(map(int, input().split())))

dx = [0,1]
dy = [1,0]


def bfs(x,y,check,tmp_data,cnt):
    
    q = deque()
    q.append((x,y))

    tmp_data[x][y] = cnt
    while q:
        x,y = q.popleft()
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if not (0 <= nx < N and 0 <= ny < N) : continue # 국경 밖
            if tmp_data[nx][ny] < 0: continue # 이미 지나쳐온 나라.

            if L <= abs(data[nx][ny] - data[x][y]) <= R: # 국경 개방 가능.
                tmp_data[nx][ny] = cnt
                q.append((nx,ny))
                check[0] = True


def cal(): 
    
    

    sum_value = 0
    for unit in united :
        x, y = unit
        sum_value += data[x][y]
    sum_value = int(sum_value/len(united))

    for unit in united:
        x, y = unit
        data[x][y] = sum_value

ans = 0
while True:
    # 모든 경우의 수에 대해서 bfs를 실행하는데 단 하나라도 안되면 끝난다.
    
    check = [False]
    cnt = -1
    tmp_data = copy.deepcopy(data)
    for i in range(N):
        for j in range(N):
            bfs(i,j,check,tmp_data)

    for i in data : print(i)
    print()
    if check[0] == False : break
    ans += 1

print(ans)
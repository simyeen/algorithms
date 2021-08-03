from collections import deque
import copy

N, L, R = map(int, input().split())

data = []
for _ in range(N): data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,tmp_data,united_list):
    
    q = deque()
    q.append((x,y))

    united = [(x,y)]
    tmp_data[x][y] = -1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0 <= nx < N and 0 <= ny < N) : continue # 국경 밖
            if tmp_data[nx][ny] < 0: continue # 이미 지나쳐온 나라.
            if L <= abs(data[nx][ny] - data[x][y]) <= R: # 국경 개방 가능.
                tmp_data[nx][ny] = -1
                q.append((nx,ny))
                united.append((nx,ny))
                
    if len(united) > 1 : united_list.append(united)

def cal(united_list):
    
    for united in united_list:
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
    cnt = -1
    tmp_data = copy.deepcopy(data)
    united_list = []
    for i in range(N):
        for j in range(N):
            bfs(i,j,tmp_data,united_list)
    cal(united_list)
    
    if len(united_list) == 0 : break
    ans += 1

print(ans)

# n^2에 대한 bfs가 전부 끝나고 연합별로 계산결과를 반영하는 cal함수를 실행해야한다.
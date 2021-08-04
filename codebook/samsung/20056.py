n = int(input())
data = [[0 for _ in range(n)]for _ in range(n)]

k = int(input())
for _ in range(k): # 사과 초기화하기.
    x, y = map(int,input().split())
    data[x-1][y-1] = 1 

l = int(input())
cmds_time, cmds_direction = [], []
for _ in range(l) : 
    arr = list(input().split())
    cmds_time.append(int(arr[0]))
    cmds_direction.append(arr[1])

def move(body):
    # 헤드를 제외하고 전부다 0으로 초기화
    x, y = body.pop(0)
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2: 
                data[x][y] = 0


def rotate(direction):
    if direction == 'L' : return 3 if d == 0 else d - 1 # 반시계방향
    elif direction == 'D': return 0 if d == 3 else d + 1 # 시계방향

dx = [-1,0,1,0]
dy = [0,1,0,-1]

x, y, time = 0, 0, 0
data[x][y] = 2
d = 1 # 처음엔 오른쪽으로 이동하니까.
body = [(0,0)]

while True: 
    nx, ny = x + dx[d], y + dy[d]

    if not (0<=nx<n and 0<=ny<n): break # 밖으로 삐져 나갈 때
    if data[nx][ny] == 2 : break # 자신의 몸과 부딪힐 떄

    if data[nx][ny] == 1 : # 사과를 먹을 때 몸 길이가 늘어난다.
        data[x][y] = 2
        body.append((nx,ny))
    else : 
        move(body)
        body.append((nx,ny))
    # 그냥 이동할떄 몸길이 head하나만 으로 줄이기
    data[nx][ny] = 2
    x, y = nx, ny 
        
    # 이 위의 과정들은 머리를 먼저 보내고 이동 했을 때
    time += 1
    if time in cmds_time: # 이동이 끝난 후에 방향 전환시켜주기
        index = cmds_time.index(time)
        direction = cmds_direction[index]
        d = rotate(direction)
    

print(time+1)
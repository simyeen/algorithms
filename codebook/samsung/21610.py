# 1번 n번 연결돼있음.
# d*s만큼 이동하기
# 물의 량 1씩 증가
# 물복사버그 마법은 대각선에 2이상인거 만큼 증가 
# 근데 이 경우는 경계 넘어가기x
# 바구니의 저장된 물의 양이 2이상이면 구름 생기고 물의 양 2감소, 구름이 생기는 칸은 3에서 구름x인 칸?

n, m = map(int, input().split())

data, cmds = [], []
for _ in range(n): data.append(list(map(int, input().split())))
for _ in range(m): 
    a, b = map(int, input().split())
    cmds.append(list((a-1,b)))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

def move(clouds,d,s):
    for i in range(len(clouds)):
        x,y = clouds[i]
        nx, ny = (x + dx[d]*s) % n, (y + dy[d]*s) % n
        clouds[i] = (nx, ny)
    
def raining(clouds):
    for i in range(len(clouds)):
        x,y = clouds[i]
        data[x][y] += 1

def replica(clouds):
    for cloud in clouds:
        x,y = cloud
        for i in range(1,8,2):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n): continue
            if data[nx][ny] == 0 : continue
            else : data[x][y] += 1

def new_clouds(clouds):
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if (i,j) in clouds : continue
            if data[i][j] >= 2: 
                new_cloud.append((i,j))
                data[i][j] -= 2
    
    while clouds: clouds.pop()
    for c in new_cloud: clouds.append(c)

for cmd in cmds:
    d, s = cmd[0], cmd[1]
    move(clouds,d,s)
    raining(clouds)
    replica(clouds)
    new_clouds(clouds)
    
ans = 0
for i in range(n):
    for j in range(n):
        ans += data[i][j]
print(ans)


n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

mv = [(0,1), (1,0), (0,-1), (-1,0)]
num_mat = [[0]*n for _ in range(n)]
orders = [(0, 0)]
x, y, step = 0, 0, 0

def check_mat(num_mat, nx, ny, n):
    if 0<=nx<n and 0<=ny<n and num_mat[nx][ny] == 0:
        return True
    return False

for cur in range(n*n-1, 0, -1):
    num_mat[x][y] = cur
    if not check_mat(num_mat, x+mv[step%4][0], y+mv[step%4][1], n):
        step += 1
    x += mv[step%4][0]
    y += mv[step%4][1]
    orders.append((x, y))

orders.reverse()

rate_left = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
rate_down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,'a',10,0],[0,0,5,0,0]]
rate_right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
rate_up = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]


def spread(data, rate_arr, nx, ny):
    global ans


    nnx, nny = -1, -1

    original_send = data[nx][ny]
    sum_send = 0
    for i in range(5):
        for j in range(5):
            if rate_arr[i][j] == 0: continue
            if rate_arr[i][j] == 'a':
                nnx, nny = i+nx-2, j+ny-2
                continue
            rx, ry = i + nx -2, j + ny - 2
            # 모래가 밖으로 나갈 떄
            send =  int((rate_arr[i][j] * data[nx][ny])/100)
            sum_send += send
            if not(0<=rx<n and 0<=ry<n):
                ans += send
            # 아직 격자 안에 남아있을 때 data 바꿔주기.
            else:
                data[rx][ry] += send

    if not(0<=nnx<n and 0<=nny<n): # 'a'마저 밖으로.
        ans += original_send - sum_send
    else:
        data[nnx][nny] += original_send - sum_send
    data[nx][ny] = 0


ans = 0
for i in range(1, len(orders)):
    nx, ny = orders[i]
    x, y = orders[i-1]


    d = (nx-x, ny-y)
    d_idx = mv.index(d)


    if d_idx == 0: # 오른쪽
        spread(data, rate_right, nx, ny)
    elif d_idx == 1: # 아래쪽
        spread(data, rate_down, nx, ny)
    elif d_idx == 2: # 왼쪽
        spread(data, rate_left, nx, ny)
    elif d_idx == 3: # 위쪽
        spread(data, rate_up, nx, ny)

print(ans)
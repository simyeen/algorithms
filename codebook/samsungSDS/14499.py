n, m, x, y, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))

dice = [0]*6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move_dice(dice, d):
    tmp = [d for d in dice]

    if d == 2: # 북쪽
        dice[0], dice[1], dice[4], dice[5] = tmp[4], tmp[0], tmp[5], tmp[1]
    elif d == 0: # 동쪽
        dice[0], dice[2], dice[3], dice[5] = tmp[3], tmp[0], tmp[5], tmp[2]
    elif d == 3: # 남쪽
        dice[0], dice[1], dice[4], dice[5] = tmp[1], tmp[5], tmp[0], tmp[4]
    elif d == 1: # 서쪽
        dice[0], dice[2], dice[3], dice[5] = tmp[2], tmp[5], tmp[0], tmp[3]

ans = []
for cmd in cmds:
    d = cmd-1
    nx, ny = x+dx[d], y+dy[d]
    if not(0<=nx<n and 0<=ny<m): continue

    move_dice(dice, d)
    x, y = nx, ny
    if data[x][y] == 0:
        data[x][y] = dice[5]

    else:
        dice[5] = data[x][y]
        data[x][y] = 0

    print(dice[0])



# 1. cmd에 따라서 주사위를 이동시킨다.
# 2. 이동할 때 move_dice 함수를 통해서 dice들의 값을 재정의한다.
# 3. dice[5] <= 가장 아랫면과 data[nx][ny]를 비교한다.
# 4. dice[0]을 출력한다.

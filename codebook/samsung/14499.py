n, m, x, y, k = map(int, input().split())

data = []
for _ in range(n): data.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0,0,0,0,0,0]

def rotate(cmd):

    if cmd == 2: # 동쪽으로 이동. 밑면은 
        three, zero, two, five = dice[3], dice[0], dice[2], dice[5]
        dice[0] = two
        dice[2] = five
        dice[5] = three
        dice[3] = zero

    elif cmd == 1: # 서쪽으로 이동.
        three, zero, two, five = dice[3], dice[0], dice[2], dice[5]
        dice[0] = three
        dice[3] = five
        dice[2] = zero
        dice[5] = two

    elif cmd == 3: # 북쪽으로 이동.
        one, zero, four, five = dice[1], dice[0], dice[4], dice[5]
        dice[0] = four
        dice[1] = zero
        dice[4] = five
        dice[5] = one

    elif cmd == 4: # 남쪽으로 이동.
        one, zero, four, five = dice[1], dice[0], dice[4], dice[5]
        dice[0] = one
        dice[1] = five
        dice[4] = zero
        dice[5] = four

for cmd in cmds:
    
    nx, ny = x + dx[cmd-1], y + dy[cmd-1]
    if not (0 <= nx < n and 0 <= ny < m) : continue

    rotate(cmd)
    if data[nx][ny] == 0 : 
        data[nx][ny] = dice[5]
    else : 
        dice[5] = data[nx][ny]
        data[nx][ny] = 0
    
    x, y = nx, ny
    
    print(dice[0])
    

    

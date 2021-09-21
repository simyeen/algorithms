# 마법사 상어와 토네이도


n = int(input())

data = []
for _ in range(n) : data.append(list(map(int, input().split())))

tornados = [[int(n/2), int(n/2)]]
directions = [[0,-1],[1,0],[0,1],[-1,0]]

i, end = 2, False
while True:
    if end == True: break        
    x, y = tornados[-1]
    
    for t in range(1,i): 
        y -= 1
        tornados.append([x,y])
        if [x,y] == [0,0] : 
            end = True
            break
    if end == True: break    
    
    for t in range(1,i): 
        x += 1
        tornados.append([x,y])
    i+=1
    
    for t in range(1,i): 
        y += 1
        tornados.append([x,y])
        
    for t in range(1,i): 
        x -= 1
        tornados.append([x,y])
        
    i+=1

send_table = [[0 for _ in range(5)] for _ in range(5)]
send_table[0][2], send_table[4][2] = 2,2
send_table[1][1], send_table[3][1] = 10,10
send_table[1][2], send_table[3][2] = 7,7
send_table[1][3], send_table[3][3] = 1,1
send_table[2][1], send_table[2][0] = 0, 5


def rotate(d):
    t = 0
    if d == 0: return send_table
    if d == 1 : t = 3
    elif d == 2: t = 2
    elif d == 3: t = 1

    ret = [s[:] for s in send_table]
    for _ in range(t):
        tmp = [[0 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                tmp[j][4-i] = ret[i][j]
        ret = [t[:] for t in tmp]
    return ret

def spread(arr, tornados, table, d):
    global ans

    x, y = tornados
    dx, dy = directions[d]
    nx, ny = x+dx, y+dy

    original_send = arr[x][y]
    arr[x][y] = -1
    rest_send = original_send

    for r in range(x-2,x+3):
        for c in range(y-2,y+3):
            i, j = r-(x-2), c-(y-2)
            send = int(original_send * (table[i][j]/100))
            if send == 0: continue
            
            if not(0<=r<n and 0<=c<n) :  # 빠져나갈 때
                ans += send
                rest_send -= send
                continue
            
            arr[r][c] += send
            rest_send -= send

    if 0<=nx<n and 0<=ny<n : arr[nx][ny] += rest_send
    else : ans += rest_send

ans = 0
arr = [d[:] for d in data]
for i in range(1, len(tornados)):
    dx = tornados[i][0] - tornados[i-1][0]
    dy = tornados[i][1] - tornados[i-1][1]

    d = directions.index([dx,dy])
    table = rotate(d)

    new_arr = spread(arr, tornados[i], table, d)

print(ans)


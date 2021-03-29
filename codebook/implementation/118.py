
n, m = map(int, input().split())
x, y, d = map(int, input().split())

data = [[0]*m for _ in range(n)] 

for i in range(n) :
    data[i] = list(map(int, input().split()))


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

result = 0

def turn_left():
    global d
    return (d+3)%4

def check(x,y):
    print('check in ', x , y)
    global d
    global result

    cnt = 0 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if data[nx][ny] == 1 : 
            cnt+=1 
            if cnt == 3 :
                x = x - dx[d]
                y = y - dx[d]
                break

    if data[x-dx[d]][y-dx[d]] == 1:
        print(result)
        exit()

while True:

    check(x,y)

    for i in range(4):
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]

        if data[nx][ny] == 1:
            break

        if data[nx][ny] == 0 :
            data[nx][ny] = 2
            x = nx
            y = ny
            result +=1
            break

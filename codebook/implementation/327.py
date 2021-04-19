n = int(input())
k = int(input())
direction = 1
arr = [[0]*(n+2) for i in range(n+2)]
for i in range(n+2):
    arr[0][i], arr[n+1][i] = -1, -1
    arr[i][0], arr[i][n+1] = -1, -1

for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1

l = int(input())
path = []
for _ in range(l):
    x, c = input().split()
    path.append((int(x),c))

r, c = 1, 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn(x):
    global direction
    if x == 'D' : 
        direction = (direction+1)%4
    elif x == 'L' :
        if direction > 1:
            direction -= 1
        else :
            direction = 3
    print('현재 d는 ', direction)

time = 0
for _ in range(20):
    print('time:',time, r,c)
    
    for i in range(k):
        if time == path[i][0]:
            turn(path[i][1])

    nr = r + dr[direction]
    nc = c + dc[direction]
    if arr[nr][nc] == -1 :
        break

    if arr[nr][nc] == 1: # 사과가 있을 때
        print(arr)
        arr[nr][nc] = 0 

    elif arr[nr][nc] == 0: # 사과가 없을 때
        r = nr
        c = nc 

    time += 1

print(time)











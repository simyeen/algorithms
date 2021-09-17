from collections import deque

n, m, oil = map(int, input().split())

data = []
for _ in range(n) : data.append(list(map(int, input().split())))
x, y = map(int, input().split())
x, y = x-1, y-1

people, dest = [],[]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    people.append((a-1, b-1))
    dest.append((c-1, d-1))
check = [[False, False] for _ in range(m)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

for i in range(m):
    arr = [d[:] for d in data]
    q = deque()
    q.append((x,y,0))
    arr[x][y] = 2
    person = -1

    if (x,y) in people:
        index = people.index((x,y))
        if check[index][0] == False:
            check[index][0] = True
            person = index

    while q:
        if person != -1 : break
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n) or arr[nx][ny] == 1: continue
            if arr[nx][ny] == 2 : continue
            if arr[nx][ny] == 0 :
                q.append((nx,ny,cnt+1))
                arr[nx][ny] = 2

                if (nx,ny) in people:
                    index = people.index((nx,ny))
                    if check[index][0] == True : continue
                    elif check[index][0] == False : 
                        check[index][0] = True    
                        person = index
                        x, y, cnt = nx, ny, cnt+1
                        break
    oil -= cnt
    if oil <= 0 or person == -1: 
        print(-1)
        exit()

    arr = []
    arr = [d[:] for d in data]
    arr[x][y] = 2
    
    cnt = 0
    dest_q = deque()
    dest_q.append((x,y,cnt))

    fx,fy = dest[person]

    find = False
    while dest_q:
        if find : break
        x, y, cnt = dest_q.popleft()
        if (x,y) == (fx,fy): break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n) or arr[nx][ny] == 1: continue
            if arr[nx][ny] == 2 : continue
            if arr[nx][ny] == 0 :
                dest_q.append((nx,ny,cnt+1))
                arr[nx][ny] = 2
                if (nx,ny) == (fx,fy):
                    x, y, cnt = nx, ny, cnt+1
                    find = True
                    break
        
    if oil - cnt < 0 or find == False: 
        print(-1)
        exit()
    else : oil += cnt
    print(x,y)

print(oil)


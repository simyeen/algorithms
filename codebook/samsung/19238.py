# 스타트 택시

# 1. 그냥 while문 하나에 사람찾기 => 목적지 찾기 2개넣음
# NameError라는 런타임에러가 발생했는데 이유를 못찾음.
# 아마 변수명이 너무 혼합돼고 그래서 터진듯

# 2. people만나자마자 바로 return 시킴
# 이 경우 그냥 dx, dy만 조건에 맞게하면 알맞은 사람을 찾을거라 착각함.
# 애초에 잘못된 사고방식.

# 3. check배열을 둬서 False인 값들은 전부다 p_list에 둔다.
# p_list를 조건에 맞게 정렬시킨 후에 값을 넣어냄.
# 얻은 값에 맞는애만 check[True] 처리해줬다.

from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n, m, oil = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))
x, y = map(int, input().split())
x, y = x-1, y-1

people, dest = [],[]
for _ in range(m):
    a,b,c,d, = map(int, input().split())
    people.append((a-1,b-1))
    dest.append((c-1,d-1))
check = [False for _ in range(m)]

def find_people(x, y, people):
    global oil

    arr = [d[:] for d in data]
    q = deque()
    q.append((x,y,0))
    arr[x][y] = 2

    if (x,y) in people:
        index = people.index((x,y))
        if check[index] == False:
            check[index] = True
            return [x,y,index]

    p_list, p_index = [], -1
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n) : continue
            if arr[nx][ny] == 1 or arr[nx][ny] == 2 : continue
            if (nx,ny) in people:
                index = people.index((nx,ny))
                if check[index] == False: p_list.append((nx,ny,dist+1))
            q.append((nx,ny,dist+1))
            arr[nx][ny] = 2 
    
    if len(p_list) == 0: return [-1,-1,-1]

    p_list.sort(key=lambda x : (x[2], x[0], x[1]))
    x, y, dist = p_list[0]
    p_index = people.index((x,y))

    oil -= dist
    if oil < 0 : return [-1,-1,-1]
    check[p_index] = True
    return [x,y, p_index]

def find_dest(p_x, p_y, destination):
    global oil

    x, y = p_x, p_y

    arr = [d[:] for d in data]
    q = deque()
    q.append((x,y,0))
    arr[x][y] = 2

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n) : continue
            if arr[nx][ny] == 1 or arr[nx][ny] == 2 : continue
            if (nx,ny) == destination:
                if oil - (dist+1) < 0 : return [-1,-1]
                oil += dist+1
                return [nx,ny]
            else :
                q.append((nx,ny,dist+1))
                arr[nx][ny] = 2 
    return [-1,-1]

def end():
    print(-1)
    exit()

for _ in range(m):
    p_x, p_y, p_index = find_people(x,y,people)
    if p_x == -1 or p_y == -1 : end()

    destination = dest[p_index]
    x, y = find_dest(p_x, p_y, destination)
    if x == -1 or y == -1 : end()

print(oil)


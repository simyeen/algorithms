# 어른 상어

n, m, k = map(int, input().split())
data = []
for _ in range(n) : data.append(list(map(int,input().split())))
sharks = []
for i in range(n):
    for j in range(n):
        if data[i][j] != 0 : sharks.append([i,j,data[i][j]-1,k])
sharks.sort(key=lambda x : x[2]) # 번호순으로 정렬시키기.

direc = list(map(int,input().split()))
for i in range(m):
    d = direc[i]-1
    sharks[i].append(d)

shark_direciton = [[] for _ in range(401)]
for shark in sharks:
    x, y, s, d, k = shark    
    for _ in range(4):
        a,b,c,d = map(int, input().split())
        shark_direciton[s].append([a-1,b-1,c-1,d-1])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

smells = [[[-1,-1] for _ in range(n)] for _ in range(n)]
for shark in sharks:
    x,y,s,k,d = shark
    smells[x][y][0], smells[x][y][1] = s, k 

def select_direction(x, y, s, d):
    global n
    d_list = shark_direciton[s][d]
    tmp_list = []
    for next_d in d_list:
        nx, ny = x + dx[next_d], y + dy[next_d]
        if not (0<=nx<n and 0<=ny<n) : continue
        if smells[nx][ny][0] == -1: return next_d # 비어있을 때
        elif smells[nx][ny][0] == s: tmp_list.append(next_d)
    return tmp_list[0]

def remove_shark(check_shark, check_list):
    for i in range(len(sharks)):
        shark = sharks[i]
        if shark[2] in check_shark: continue
        else : check_list[i] = True
        
t, check_list = 0, [False for _ in range(401)]
#while True:
for _ in range(31):
    for d in data : print(d)
    print()
    for s in smells : print(s)
    print()

    if t > 1000: break
    for check in check_list[1:] :
        if check == True : continue
        else : break
    else : 
        print(t)
        exit()
            
    next_list = []
    for shark in sharks: # 상어 이동시키기.
        x, y, s, k, d = shark
        if check_list[s] == True: continue
        nd = select_direction(x, y, s, d)
        nx, ny = x + dx[nd], y + dy[nd] # 무조건 이쪽으로 이동하면 됨.
        next_list.append([nx,ny,s,k,nd])
        data[x][y] = 0

    dict = {} # 일단 이동시키고 중복제거하기.
    for next in next_list:
        x, y, s, k, d = next
        key = str(x)+str(y)
        if key not in dict: dict[key] = [s, d]
        elif key in dict:
            if dict[key][0] > s: dict[key] = [s, d]
    
    check_shark = []
    for key in dict: # dict에 있는 상어만 이동하고 나머진 shark에서 제거.
        nx, ny, s, nd = int(key[0]), int(key[1]), dict[key][0], dict[key][1] 
        if s == 0 : data[nx][ny] = -1
        else : data[nx][ny] = s

        smells[nx][ny][0], smells[nx][ny][1] = s, k # 이렇게 하면 하나만 담김.
        check_shark.append(s)
        for i in range(5):
            if i == 0 : sharks[s][i] = nx
            elif i == 1 : sharks[s][i] = ny
            elif i == 4 : sharks[s][i] = nd

    remove_shark(check_shark,check_list)

    for i in range(n):
        for j in range(n):
            key = str(i)+str(j)
            if key in dict : continue
            if smells[i][j][0] == -1: continue
            if smells[i][j][1] == 1 : 
                smells[i][j][0] = -1
                smells[i][j][1] = -1
            else : smells[i][j][1] -= 1

    t += 1 
print(-1)

# 1. 기존의 배열을 append나 pop할때는 잘 고려해야 한다.
# 2. 특히 전역이라면 함수가 계속 바뀔 수 있어서 지양하자.
# 3. remove하는 것은 왠만해선 checklist를 이용하자.
# 4. 문제가 복잡할수록 모듈화를 잘 시켜야 디버깅 할 수 있다.
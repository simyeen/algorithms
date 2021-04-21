n = int(input())
data = [[2]*(n+1) for i in range(n+1)]
result = []

build_frame = []
for i in range(8):
    x, y, a, b = map(int, input().split())
    x, y = y, x
    build_frame.append([x,y,a,b])
    

dr = [-1, 0]
dc = [0, 1]

def insert(frame):
    
    r, c = frame[0], frame[1]
    kind = frame[2]
    nr, nc = frame[0] + dr[kind], frame[1] + dc[kind]
    if kind == 0: # 기둥 설치
        if r == n or data[r][c] == 0 or data[r][c] == 1: # 바닥이거나 설치할 위체 기둥이나 보가 존재할 때
            data[r][c] = 0 # 설치 
            data[nr][nc] = 0
            result.append([r, c, kind]) 
        else :
            print('기둥을 설치 할 수 없는 자리입니다.', r, c)
            print(data)         
    elif kind == 1: # 보 설치
        if r != n and (data[r][c] == 0 or data[r][c] == 1 and data[nr][nc] == 1) :
            data[r][c] = 1
            data[nr][nc] = 1
            result.append([r, c, kind])
    print(r,c,kind)
    print(result)

def delete(frame):
    r, c = frame[0], frame[1]
    kind = frame[2]
    nr, nc = frame[0] + dr[kind], frame[1] + dc[kind]

    if kind == 0:
        pass
    else :pass 

def solution():
    
    for i in range(len(build_frame)):
        if build_frame[i][3] == 0:
            delete(build_frame[i])
        else :
            insert(build_frame[i])

solution()
print(result)
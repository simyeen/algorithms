n = int(input())
data = [[2]*(n+1) for i in range(n+1)]
result = []

build_frame = []
for i in range(10):
    x, y, a, b = map(int, input().split())
    x, y = n-y, x
    build_frame.append([x,y,a,b])
    

dr = [-1, 0]
dc = [0, 1]

def insert(frame):
    global n    
    r, c = frame[0], frame[1]
    kind = frame[2]
    nr, nc = frame[0] + dr[kind], frame[1] + dc[kind]
    if kind == 0: # 기둥 설치
        if r == n or data[r][c] == 0 or data[r][c] == 1: # 바닥이거나 설치할 위체 기둥이나 보가 존재할 때
            data[r][c] = 0 # 설치 
            data[nr][nc] = 0
            result.append([c, n-r, kind]) 
        else :
            print('기둥을 설치 할 수 없는 자리입니다.', r, c)
            print(data)         
    elif kind == 1: # 보 설치
        if r != n and (data[r][c] == 0 or data[nr][nc] == 0 or data[r][c] == 1 or data[nr][nc] == 1) :
            data[r][c] = 1
            data[nr][nc] = 1
            result.append([c, n-r, kind])
        else :
            print('보를 설치할 수 없는 자리입니다.', c, n-r)
            print(data)
    print(result)

def delete(frame):
    global n
    r, c = frame[0], frame[1]
    kind = frame[2]
    nr, nc = frame[0] + dr[kind], frame[1] + dc[kind]
    nr2, nc2 = nr + dr[kind], nc + dc[kind]
    check1 = data[nr + dr[1]][nc + dc[1]]
    check2 = data[nr - dr[1]][nc - dc[1]]
    check3 = data[r + dr[0]][c + dc[0]]
    check4 = data[nr + dr[0]][nc + dr[0]]

    if kind == 0: # 기둥삭제
        if data[r][c] == 0 and data[nr2][nc2] != 0: # 기둥위에 기둥이 존재할 시,
            data[r][c] = 2
            result.remove([c, n-r, kind])
        if check1 == 2 and check2 ==2 : # 기둥위 양 옆이 
            data[r][c] = 2
            result.remove([c, n-r, kind])
        print('기둥을 삭제할 수 없는 자리입니다.')
        return 0

    elif kind == 1:
        if data[]

def solution():
    
    for i in range(len(build_frame)):
        if build_frame[i][3] == 0:
            delete(build_frame[i])
        else :
            insert(build_frame[i])

solution()
answer = sorted(result, key = lambda x : x[0])
print(answer)
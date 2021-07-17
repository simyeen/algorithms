from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def init(place):
    data = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                data.append((i,j))
    return data

def bfs(x,y,place):
    

    mymap = [list(list(i)) for i in place]

    q = deque()
    q.append((x,y,0)) # 처음 start할 때 
    mymap[x][y] = 'X'

    while q:
        x, y, dist = q.popleft()
        if dist >= 3 : continue # 이미 거리가 3이상이면 안전함.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx > 4 or 0 > ny or ny > 4: 
                continue # 범위를 벗어날 때
            if mymap[nx][ny] == 'X' : continue
            if mymap[nx][ny] == 'O': 
                mymap[nx][ny] = 'X'
                q.append((nx,ny,dist+1)) 
                continue
            if mymap[nx][ny] == 'P' and dist+1 <= 2: # 이 place는 망함
                return False
    return True

def solution(places):
    answer = []
    
    for place in places: # 각 place마다 검사
        data = []
        data = init(place) # 검사할 좌표 초기화
        for x, y in data: # 모든 P마다 bfs실행
            if bfs(x,y,place) == False:
                answer.append(0)
                break
        else : answer.append(1)
            
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
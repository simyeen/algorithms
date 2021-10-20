from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


data = [[] for _ in range(4)]

for i in range(4):
    fish_data = list(map(int, input().split()))
    for f in range(0, len(fish_data)-1, 2):
        data[i].append([fish_data[f], fish_data[f+1]-1])

ans = data[0][0][1]
data[0][0][0] = 0 # 0은 상어의 index


def next_d(x, y, data, d): # 상어 및 벽 검사
    for n_d in range(d, d+8):
        n_d %= 8
        nx, ny = x+dx[n_d], y+dy[n_d]

        if not(0<=nx<4 and 0<=ny<4) or data[nx][ny][0] == 0: continue
        return n_d
    return -1

def next_shark_d(x, y, data, d): # 상어 및 벽 검사
    for n_d in range(d, d+8):
        n_d %= 8
        nx, ny = x+dx[n_d], y+dy[n_d]

        if not(0<=nx<4 and 0<=ny<4) or data[nx][ny][0] == -1: continue
        return n_d
    return -1


def fish_move(data):
    idx = 1

    while idx < 17:
        flag = False
        for x in range(4):
            if flag : break
            for y in range(4):
                if data[x][y][0] == idx: # 찾는 인덱스면 이동하자.
                    n_d = next_d(x, y, data, data[x][y][1])
                    if n_d == -1: # 이동 불가능일 때
                        flag = True
                        break
                    data[x][y][1] = n_d
                    nx, ny = x+dx[n_d], y+dy[n_d]
                    data[nx][ny][0], data[x][y][0] = data[x][y][0], data[nx][ny][0]
                    data[nx][ny][1], data[x][y][1] = data[x][y][1], data[nx][ny][1]
                    flag = True
                    break
        idx += 1

    print('물고기 이동 ', idx)
    for d in data: print(d)
    print()

def shark_move():
    global ans

    while True:
        flag = False
        for x in range(4):
            if flag: break
            for y in range(4):
                if data[x][y][0] == 0: # 상어면 이동한다.
                    n_d = next_d(x, y, data, data[x][y][1])
                    if n_d == -1: # 이동 불가능일 때
                        return
                        break
                    # 상어가 이동가능 할 때
                    data[x][y][0] = -1


                    flag = True
                    break


    return False

while True:
    fish_move(data)
    if shark_move() == False:
        break

print(ans)
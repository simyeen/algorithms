# up, right, down, left 순서
# 행, 열이 아닌 (x,y)좌표임에 주의.
dx = [-1,0,1,0] 
dy = [0,1,0,-1]
dict = {'U' : 0, 'R' : 1 , 'D' : 2, 'L' : 3}
check = []

def check_path(x,y,nx,ny):
    for path in check:
        if (x,y,nx,ny) in path : return False
    return True

def solution(dirs):
    data = [[False for _ in range(11)] for _ in range(11)]
    x, y = 5, 5

    cnt = 0
    for i in dirs:
        nx = x + dx[dict[i]]
        ny = y + dy[dict[i]]

        if 0 <= nx <= 10 and 0 <= ny <= 10:
            if check_path(x,y,nx,ny): 
                cnt += 1 # 4가지 좌표를 기억하기
                check.append(((x,y,nx,ny),(nx,ny,x,y))) # 이동한 길 check하기.
            x, y = nx , ny # 이동하기

    return cnt

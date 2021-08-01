# 로봇 청소기
# r,c 입력받기

# 이동할 수 있으면 이동 => 청소 한 것
# 현재 위치에서 자신의 방향의 왼쪽부터 검색 => 현재 방향 d를 저장해두기
# 일단 돌고 청소 안된 공간이면 이동하기
# 청소 안되면 4방향 전부다 뒤지기
# cnt == 4 되버리면 그냥 뒤로 빠꾸치기
# 빠꾸 불가능 하면 종료

import copy
from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = 0

data = []
for _ in range(n): data.append(list(map(int, input().split())))
clear_data = copy.deepcopy(data)

def rotate(d):
    pass

while True :

    q = deque()
    q.append((x,y))
    clear_data[x][y] = 2 # 청소한 곳은 2로 표시

    while q:
        x, y = q.pop()

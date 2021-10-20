from itertools import product
import copy

n, m = map(int,input().split())

data = []
for _ in range(n) : data.append(list(map(int, input().split())))

cctvs = []
for i in range(n):
    for j in range(m):
        if 0< data[i][j] <6 :
            cctvs.append((i,j,data[i][j]-1))

all_kinds = [[0,1,2,3],[0,1],[0,1,2,3],[0,1,2,3],[0]]
kinds = []
for cctv in cctvs: kinds.append(all_kinds[cctv[2]])

products = list(product(*kinds)) # cctv의 모든 방향들에 대해서

up,right,down,left = [-1,0],[0,1],[1,0],[0,-1]

d = [
        [
            [up],[down],[right],[left]
        ],
        [
            [up,down], [right,left]
        ],
        [
            [up,right],[up,left],[down,right],[down,left]
        ],
        [
            [down,right,left],[up,right,left],[up,down,left],[up,down,right]
        ],
        [
            [up,down,right,left]
        ]
    ]

def count(tmp) :
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0 : cnt +=1
    return cnt


ans = []
for direction in products: # 모든 방향의 조합에 관하여
    tmp = copy.deepcopy(data)
    for i in range(len(direction)): # pro와 cctvs의 길이는 일치한다.
        cctv = cctvs[i]
        for j in range(len(d[cctv[2]][direction[i]])): # 2줄기이상으로 뻗어나갈 때
            x,y = cctv[0], cctv[1]
            dx, dy = d[cctvs[i][2]][direction[i]][j]
            nx, ny = x + dx, y + dy
            while True:
                if not (0<=nx<n and 0<=ny<m): break # 범위 안에 서만
                if data[nx][ny] == 6 : break # 벽에 막힐 떄 까지
                if 0 <= data[nx][ny] <= 5: # 감시가능 혹은 cctv일 떄
                    if data[nx][ny] == 0 : tmp[nx][ny] = -1
                    nx, ny = nx+dx, ny+dy
    ans.append(count(tmp))

print(min(ans))
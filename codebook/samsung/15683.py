import copy
from itertools import product

n, m = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))

cctvs = []
for i in range(n):
    for j in range(m):
        if 0 < data[i][j] < 6 :
            cctvs.append((data[i][j]-1, i, j))

up = (-1,0)
right = (0,1)
down = (1,0)
left = (0,-1)

directions =[   [(up),(right),(down),(left)],
                [(up,down),(right,left)],
                [(up,right),(right,down),(left,down),(left,up)],
                [(left,up,right),(up,right,down),(left,down,right),(up,left,down)],
                [(up,right,down,right)]
            ]

all_lists = [[0,1,2,3],[0,1],[0,1,2,3],[0,1,2,3],[0]] # 각 cctv종류 별 경우의 수.

def count_nodes(tmp_data):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_data[i][j] == 0: cnt +=1
    return cnt

product_lists = [] # 종류별로 나올 수 있는 경우의 수 구하기.
for cctv in cctvs:
    kind,x,y = cctv
    product_lists.append(all_lists[kind])

products = list(product(*product_lists)) # 나올 수 있는 모든 경우의 수
ans = []

for pro in products:
    tmp_data = copy.deepcopy(data)
    
    for i in range(len(pro)):
        d = pro[i] # 유동적인 값
        kind, x, y = cctvs[i][0], cctvs[i][1], cctvs[i][2] # 고정 값
        
        for direction in (directions[kind][d]): # 종류의 방향 수 만큼 (ex) 종류 2는 2방향으로 뻗어나감.
            
            print('방향',direction)
            print(directions[kind][d])
            dx, dy = direction
            nx, ny = x + dx, y + dy
            for _ in range(128):
            #while True:
    
                if not (0 <= nx < n and 0 <= ny <m) : break 
                if tmp_data[nx][ny] == 6 : break

                if tmp_data[nx][ny] == 0 :
                    tmp_data[nx][ny] = -1
                    x, y = nx, ny            
                    nx, ny = x + dx, y + dy
        for i in tmp_data:
            print(i)
        print()
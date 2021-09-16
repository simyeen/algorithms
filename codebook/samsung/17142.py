from itertools import combinations
from collections import deque

n, m = map(int, input().split())
data, viruses = [], []
for _ in range(n) : data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

original_arr = [['' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 : original_arr[i][j] = '-'
        elif data[i][j] == 0 : original_arr[i][j] = 'O'
        else : 
            original_arr[i][j] = '*'
            viruses.append((i,j)) 

combination = list(combinations(viruses, m))

ans = []
for combi in combination:    
    max_value = -1e9
    arr = [item[:] for item in original_arr]
    q = deque()
    for virus in combi:
        x, y = virus
        arr[x][y] = 0
        q.append((x,y,0))

    passive_virus = []
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0<=nx<n and 0<=ny<n) : continue
            if arr[nx][ny] == '-' : continue
            if arr[nx][ny] == 'O' or arr[nx][ny] == '*': 
                arr[nx][ny] = dist+1
                q.append((nx,ny,dist+1))
                max_value = max(max_value, dist+1)

    max_value = 0
    for i in range(n):
        for j in range(n):
            if (i,j) in viruses : arr[i][j] = '*'
            if str(type(arr[i][j])) == "<class 'int'>":
                max_value = max(arr[i][j], max_value)

    for item in arr : # 꽉 채우기 실패
        if 'O' in item : 
            max_value = -1

    ans.append(max_value)
    

if -len(ans) == sum(ans): print(-1)
else : 
    answer = 1e9
    for an in ans : 
        if an == -1 : continue
        answer = min(answer, an)
    print(answer)



# 1. virus m개를 뽑고 활성 바이러스로 본다.
# 2. 활성바이러스를 넣고 bfs시킨다.
# 3. 비활성바이러스는 활성바이러스를 만나면 활성화 된다.
# 4. 









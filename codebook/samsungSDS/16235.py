# 봄 - 여름 - 가을 - 겨울 각 단계별 함수 짜기.
# 봄 => 여름 => 가을 해버리면 양분이 들어가서 독립적이지 못함


dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def spring(data, trees_data):
    # data에서 양분 빼먹고,

    dead_list = []
    for i in range(n):
        for j in range(n):
            if len(trees_data[i][j]) == 0: continue
            trees_data[i][j].sort()
            trees = trees_data[i][j]
            for t in range(len(trees)):
                if trees[t] <= data[i][j]: #양분 먹기 가능.
                    data[i][j] -= trees[t]
                    trees_data[i][j][t] += 1
                else:
                    if t == 0:
                        trees_data[i][j] = []
                    else:
                        trees_data[i][j] = trees[:t]
                    for age in trees[t:]:
                        dead_list.append([i, j, age])
                    break

    return dead_list

def summer(data, dead_list):
    for x, y, age in dead_list:
        data[x][y] += int(age/2)

def fall(trees_data):
    for i in range(n):
        for j in range(n):
            trees = trees_data[i][j]
            if len(trees_data[i][j]) == 0: continue
            for tree in trees:
                if tree % 5 == 0:
                    for d in range(8):
                        nx, ny = i+dx[d], j+dy[d]
                        if not(0<=nx<n and 0<=ny<n): continue
                        trees_data[nx][ny].append(1)

def winter(data):
    for i in range(n):
        for j in range(n):
            data[i][j] += A[i][j]

n, m, k = map(int, input().split())
data, A = [[5 for _ in range(n)] for _ in range(n)], []
for _ in range(n): A.append(list(map(int, input().split())))

trees_data = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c= map(int, input().split())
    trees_data[a-1][b-1] = [c]

for _ in range(k):
    dead_list = spring(data, trees_data)
    summer(data, dead_list)
    fall(trees_data)
    winter(data)

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees_data[i][j])
print(ans)


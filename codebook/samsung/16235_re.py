n, m, k = map(int, input().split())

energy, A = [[5 for _ in range(n)] for _ in range(n)], []
for _ in range(n) : A.append(list(map(int, input().split())))

trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(k):

    summer_list = []
    for i in range(n):
        for j in range(n):
            tree = trees[i][j]
            if len(tree) == 0 : continue
            if len(tree) == 1 and tree[0] <= energy[i][j]: 
                energy[i][j] -= tree[0]
                tree[0] += 1
            else :
                index = -1
                tree.sort()
                for k in range(len(tree)):
                    t = tree[k]
                    if t <= energy[i][j]:
                        energy[i][j] -= t
                        tree[k] += 1
                    else : 
                        index = k
                        break
                if index != -1 : summer_list.append((i,j,k))
    
    for summer in summer_list:
        i,j,k = summer
        tree = trees[i][j]
        for t in tree[k:]: energy[i][j] += int(t/2)
        trees[i][j] = tree[:k]
    
    for i in range(n):
        for j in range(n):
            tree = trees[i][j]
            if len(tree) == 0 : continue
            for t in tree:
                if t%5 != 0 : continue
                for k in range(8):
                    nx, ny = i+dx[k], j+dy[k]
                    if not(0<=nx<n and 0<=ny<n) : continue
                    trees[nx][ny].append(1)
  
    for i in range(n):
        for j in range(n): energy[i][j] += A[i][j]
                    
ans = 0
for i in range(n):
    for j in range(n):
        tree = trees[i][j]
        ans += len(tree)
print(ans)
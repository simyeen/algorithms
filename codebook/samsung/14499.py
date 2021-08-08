n, m, x, y, k = map(int, input().split())

cmds = []
for _ in range(n): 
    cmds.append(list(map(int, input())))

d = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]


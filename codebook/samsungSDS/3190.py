from collections import deque

n = int(input())
k = int(input())

data = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    data[a-1][b-1] = 2
l = int(input())
cmds = []
for _ in range(l):
    a, b = input().split()
    cmds.append((int(a), b))

def change_d(d, dir):
    if dir == 'L' : return (d-1)%4
    else : return (d+1)%4

q = deque()
q.append([0, 0])
data[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t, d = 0, 1
while True:
    x, y = q[-1]
    nx, ny = x+dx[d], y+dy[d]
    if not(0<=nx<n and 0<=ny<n): break # 밖으로 나갈 때
    if data[nx][ny] == 1: break # 몸통에 부딪힐 떄

    if data[nx][ny] == 0: # 사과 없을 때 그대로 이동.
        t_x, t_y = q.popleft()
        data[t_x][t_y] = 0

    data[nx][ny] = 1
    q.append([nx, ny])
    t += 1
    for time, direction in cmds:
        if t == time:
            d = change_d(d, direction)
print(t+1)


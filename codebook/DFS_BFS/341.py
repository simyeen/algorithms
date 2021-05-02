from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
arr = []

empty_rooms = []
block = []
virus = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty_rooms.append((i, j))
        elif arr[i][j] == 1:
            block.append((i, j))
        else :
            virus.append((i, j))

candidates = list(combinations(empty_rooms,3))

def make_block(new_arr, candidate):
    for i, j in candidate:
        new_arr[i][j] = 1

def bfs(new_arr, x, y):

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if new_arr[nx][ny] == 1:
                continue
            if new_arr[nx][ny] == 2:
                continue
            elif new_arr[nx][ny] == 0 :
                new_arr[nx][ny] = 2
                q.append((nx, ny))

def check(new_arr):
    count = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0:
                count += 1
    return count

max_value = 0
for candidate in candidates:
    new_arr = copy.deepcopy(arr)
    make_block(new_arr, candidate)
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 2:
                bfs(new_arr, i, j)
    new_value = check(new_arr)
    max_value = max(max_value, new_value)
    
print(max_value)






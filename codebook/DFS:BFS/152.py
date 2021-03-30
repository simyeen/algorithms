from collections import deque

row, col = map(int, input().split())

arr = []
for _ in range (row) :
    arr.append(list(map(int, input())))

dist = 1

def bfs(x,y):
    queue = deque([x, y, dist])
    print("before row, col, dist = ", x, y, dist)
    
    while queue :
        v = queue.popleft()
        
        if not arr[x-1][y] == 0 :
            queue.append([x-1, y, dist+1])
        if not arr[x+1][y] == 0 :
            queue.append([x+1, y, dist+1])
        if not arr[x][y-1] == 0 :
            queue.append([x, y-1, dist+1])
        if not arr[x][y+1] == 0 :
            queue.append([x, y+1, dist+1])
            

bfs(1,1)
print(cnt)
import copy
from itertools import combinations

n = int(input())

data = []
for _ in range(n):
    data.append(input().split())

students = []
teachers = []
emptys = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 'S':
            students.append((i,j))
        elif data[i][j] == 'T':
            teachers.append((i,j))
        else :
            emptys.append((i,j)) 

blocks = list(combinations(emptys, 3))

def get_block(temp, block):
    for i, j in block:
        temp[i][j] = 'O'    
    
def check(temp):
    for x, y in teachers:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx and nx < n and 0 <= ny and ny < n:
                if temp[nx][ny] == 'S':                    
                    return False
                elif temp[nx][ny] == 'O':
                    break
                else : 
                    nx = nx + dx[i]
                    ny = ny + dy[i]
    return True

for block in blocks:
    temp = copy.deepcopy(data)
    get_block(temp, block)
    if check(temp) == True:
        print('YES')
        exit()

print('NO')        
        

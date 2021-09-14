# 사다리 조작 1시간 50분
# 실패 => 다시하기.
from itertools import combinations
import copy

def simulation(arr,n,m): # return 값이 m값이니?
    
    starts, ans = [(0,i) for i in range(m)], []
    for start in starts:
        x, y = start
        check = False
        while True:
            if x == n : 
                if y == start[1] : 
                    ans.append(y)
                    break
                else : return False
            if arr[x][y] == 0 or check == True: # 아래로 이동
                x += 1 
                check = False
                continue
            else : 
                if 0 <= y-1 and arr[x][y-1] == arr[x][y]:                    
                    y -= 1
                    check = True
                elif y+1 < m and arr[x][y+1] == arr[x][y]: 
                    y += 1
                    check = True
    answer = [c for c in range(m)]

    if answer == ans : return True
    return False

# [1, 1, 2, 2, 0]
# [0, 0, 1, 1, 0]
# [0, 1, 1, 0, 0]
# [0, 0, 0, 0, 0]
# [1, 1, 0, 1, 1]
# [0, 0, 0, 0, 0]

def new_ladders(data, combi): # 가로선 추가
    tmp_arr = copy.deepcopy(data)
    for i in range(len(combi)):
        x, y = combi[i]
        tmp_arr[x][y], tmp_arr[x][y+1] = i+2, i+2
    return tmp_arr

N, M, H = map(int, input().split())

n, m = H, N
data = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(M): 
    a, b = map(int, input().split())
    data[a-1][b-1], data[a-1][b] = 1, 1

candidates = []
for i in range(n):
    for j in range(m-1):
        if data[i][j] == 0 and data[i][j+1] == 0 : candidates.append((i,j))

for i in range(1,4):
    combination = list(combinations(candidates,i))
    if i == 1 : 
        for combi in combination:
            arr = new_ladders(data,combi)
            if simulation(arr,n,m) == True: 
                print(i)
                exit()
    else :
        for combi in combination:
            for a, b in combi: # 연속된 가로선 거르기.
                if (a,b+1) in combi : break
            else : 
                arr = new_ladders(data,combi)
                if simulation(arr,n,m) == True:
                    print(i)
                    exit()    
print(-1)



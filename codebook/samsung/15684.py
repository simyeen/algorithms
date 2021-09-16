# 사다리 문제 => timeout

from itertools import combinations

N, M, H = map(int, input().split())
n, m = H, N # n은 행의 개수, m은 열의 개수
data = [[0 for _ in range(m)] for _ in range(n)]

cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    data[a][b], data[a][b+1] = cnt, cnt
    cnt += 1

candidates = []
for i in range(n):
    for j in range(m-1):
        if data[i][j] == 0 and data[i][j+1] == 0 : candidates.append((i,j))

def check(new_arr, n, m) : 

    starts = [(0,col) for col in range(m)]
    end, ans = [i for i in range(m)], []

    for start in starts:
        x, y = start
        flag = False
        while True:
            if x == n: # 끝에 도달
                if y != start[1] : return False
                ans.append(y)
                break  

            if flag or new_arr[x][y] == 0: # 아래로 이동
                x += 1
                flag = False
                continue
            
            if 0 <= y-1 < m and new_arr[x][y] == new_arr[x][y-1]: 
            # 왼쪽 이동
                y -= 1    
                flag = True
                continue
            if 0 <= y+1 < m and new_arr[x][y] == new_arr[x][y+1]: 
            # 오른쪽 이동
                y += 1
                flag = True
                continue

    if ans == end : return True
    return False

def new_ladders(data, combi, cnt): # 새로운 가로선 추가된 배열 return
    for a,b in combi: # i가 2이상 일때 검사된다.
        if (a, b+1) in combi: return []

    new_arr = [item[:] for item in data]    
    for i in range(len(combi)):
        a, b = combi[i]
        new_arr[a][b], new_arr[a][b+1] = i+cnt, i+cnt

    return new_arr

if check(data, n, m) == True:
    print(0)
    exit()

for i in range(1, 4):
    combination = list(combinations(candidates,i))
    for combi in combination:
        new_arr = new_ladders(data,combi, cnt)
        if len(new_arr) == 0: continue # combi가 2, 3 일때 이상한 애들
        if check(new_arr, n, m) == True:
            print(i)
            exit()
print(-1)

# i번 세로선의 결과가 i번으로 떨어지게 하자
# 추가해야 할 가로선 개수의 최솟값은?
# 사다리 초기화

# 가로선을 넣을 좌표 1, 2, 3개 
# i번에서 i번으로 출발시키기.


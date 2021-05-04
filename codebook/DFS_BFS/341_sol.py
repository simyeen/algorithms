# 내가 푼 풀이라 똑같은데 답지는 bfs대신에 dfs를 사용했다.

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n) :
    data.append(list(map(int, input().split())))
# 시계방향
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

result = 0

# nx, ny 부터 만들고 checking 하자
def virus(x, y):
    for i in range(4):
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < n and ny >= 0 amd ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return 

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
def check(visited, n, m):
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                return False
    return True

def solution(rows, columns):
    n, m = rows, columns

    visited = [[False for _ in range(m)] for _ in range(n)]
    data = [[0 for _ in range(m)] for _ in range(n)]

    x, y, cnt = 0, 0, 1
    data[x][y] = cnt

    q = [(x,y)]
    while True:
        x, y = q.pop()

        # nx, ny 배정하기 전에 체크 하기.
        if check(visited, n, m):
            return data

        if cnt % 2 == 0:
            nx, ny = (x+1) % n, y
        else:
            nx, ny = x, (y+1) % m

        cnt += 1
        # 이동하기 전에 검사 => 다시 처음으로 돌아올 때
        if (nx, ny) == (0, 0):
            if data[0][0] % 2 == cnt % 2:
                return data

        q.append((nx, ny))
        data[nx][ny] = cnt
        visited[nx][ny] = True


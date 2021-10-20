from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next


def bomb(x,y, arr):
    q = deque()
    q.append((x, y, arr[x][y]))
    arr[x][y] = 0
    while q:
        x, y, value = q.popleft()
        for i in range(4):
            for d in range(1, value):
                nx, ny = x + dx[i]*d, y + dy[i]*d
                if not(0<=nx<n and 0<=ny<m): continue
                if arr[nx][ny] > 1:
                    q.append((nx, ny, arr[nx][ny]))
                arr[nx][ny] = 0


def sorted_data(arr):
    new_data = [[0 for _ in range(m)] for _ in range(n)]
    tmp_data = []

    for j in range(m):
        tmp = ''
        for i in range(n):
            if arr[i][j] != 0:
                tmp += str(arr[i][j])
        tmp = tmp.zfill(n)
        tmp_data.append(list(tmp))

    for i in range(m):
        for j in range(n):
            new_data[j][i] = int(tmp_data[i][j])

    return new_data


T = int(input())
for t in range(1, T+1):
    k, m, n = map(int, input().split())
    data, arr = [], [i for i in range(m)]
    for _ in range(n): data.append(list(map(int, input().split())))

    ans = 1e9
    for pro in product(arr, k):
        bomb_data = [d[:] for d in data]
        for p in pro: # pro는 m개의 열들의 중복순열
            for i in range(n):
                if bomb_data[i][p] != 0:
                    bomb(i, p, bomb_data)
                    bomb_data = sorted_data(bomb_data)
                    break

        tmp_ans = 0
        for i in range(n):
            for j in range(m):
                if bomb_data[i][j] != 0:
                    tmp_ans += 1
        ans = min(ans, tmp_ans)

    print('#%d' %t, ans)


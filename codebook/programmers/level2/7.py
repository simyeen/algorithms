from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def solution(maps):
    r, c, cnt = 0, 0, 1

    q = deque()
    q.append((r,c,cnt))
    n, m = len(maps), len(maps[0])

    while q :
        r, c, cnt = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if nr == n-1 and nc == m-1 :
                    return cnt +1 
                if maps[nr][nc] == 1:
                    q.append((nr, nc, cnt+1))
                    maps[nr][nc] = 0
    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
print(solution(maps))
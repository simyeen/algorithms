N, M = map(int, input().split())

num = [i+1 for i in range(N)]
check = [False for i in range(N)]
arr = []


def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return

    for i in range(N):
        arr.append(num[i])
        dfs(cnt+1)
        arr.pop()


dfs(0)

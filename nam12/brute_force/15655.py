N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

check = [False for i in range(N)]
ans = []


def dfs(cnt):

    if cnt == M:
        print(*ans)
        return

    for i in range(N):

        if (check[i]):
            continue

        check[i] = True
        ans.append(num[i])
        dfs(cnt+1)
        ans.pop()
        for j in range(i+1, N):
            check[j] = False


dfs(0)

N = int(input())

arr = [[] for i in range(N)]
for i in range (N) :
    arr[i] = list(map(int, input().split()))

goal = 1
for i in range(int(N/2)+1, N+1, 1):
    goal *= i
goal = int(goal/2)

visited = [False for i in range (N+2)]

tmp = []
ans = 999999
def go(cnt, diff) :

    global ans 
    if cnt == int(N/2) :
        
        ans = min(ans, diff)
        return

    for i in range (int(N/2)-1) :
        if visited[i] :
            continue

        visited[i]= True
        tmp.append(i)
        go(cnt+1, diff)
        for j in range(i+1, int(N/2)-1):
            visited[j] = False


go(0,0)
print(ans)
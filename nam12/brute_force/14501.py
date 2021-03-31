n = int(input())
time, pay = [0 for i in range (n+10)], [0 for i in range (n+10)]
check_list = [False for i in range(n)]
ans = []

for i in range(n) :
    time[i] , pay[i] = map(int, input().split())


ans = -1

def dfs(cnt, sum):
    global ans

    if cnt > n : return
    if cnt == n : 
        ans = max(sum, ans)
        return  

    dfs(cnt + time[cnt], sum + pay[cnt])
    dfs(cnt + 1, sum)


dfs(0, 0) 
print(ans)





 



def dfs( sum, n ) :
    if sum > n : return 0
    if sum == n : return 1

    now = 0 
    for i in range (1,4):
        now += dfs( sum + i, n ) 
    return now

t = int(input())
for i in range (t) :
    n = int(input())
    print(dfs(0, n))    
    
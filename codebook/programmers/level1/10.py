d = [1,3,2,5,4]
budget = 9
check = [False] * len(d)
max_value = -1e9

def dfs(cnt, budget):
    global max_value

    if budget == 0:
        max_value = max(max_value, cnt)
        return 

    for i in range(len(d)) :
        if check[i] == False:
            check[i] = True
            dfs(cnt+1, budget - d[i])
            check[i] = False


def solution(d, budget):
    answer = 0
    d.sort()

    dfs(0, budget)
    answer = max_value
    
    return answer

print(solution(d, budget))


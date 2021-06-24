cnt = 0
check = [False for _ in range(6)]

def dfs(numbers,target,sum_value):
    global cnt
    print(sum_value, check)
    if sum_value == target:
        cnt += 1
        return
    
    for i in numbers:
        if check[i] == False:
            check[i] = True
            dfs(numbers,target,sum_value-i)            
            check[i] = False
            
            
def solution(numbers, target):
    # check = [False for _ in range(len(numbers)+5)]
    dfs(numbers,target,sum(numbers))
    return cnt

print(solution([1,1,1,1,1],3))
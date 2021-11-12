arr = [1,2,3]
result = []
check = [False] * len(arr)

cnt = 0
ans = []
def dfs(level, r):
    global cnt
    if level == r:
        print(result)    
        cnt += 1
        return 
    for i in range(len(arr)):
        if check[i] == True: continue
        result.append(arr[i])
        check[i] = True
        dfs(level+1, r)
        result.pop()
        check[i] = False


arr = [1,2,3,4,5]
r = 2
def dfs_c(level, begin):
    if level == r:
        print(result)
        return
    for i in range(begin, len(arr)):
        result.append(arr[i])
        dfs_c(level+1, i+1)
        result.pop()
dfs_c(0,0)


def dd(cnt):
    if 
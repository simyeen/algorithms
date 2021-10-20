n, k = map(int, input().split())


def check_cnt(arr, index, case, flag):
    global k
    if case == 0:
        target = arr[index]
        for i in range(index, index-k, -1):
            if not (0<=i<n) or flag[i] or target != arr[i]:
                return False
            flag[i] = True
        return True
    else:
        target = arr[index+1]
        for i in range(index+1, index+k+1):
            if not (0<=i<n) or flag[i] or target != arr[i]:
                return False
            flag[i] = True
        return True

def check_path(arr):
    global n
    flag = [False for _ in range(n)]
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        if arr[i]+1 == arr[i+1] : # 다음 구간이 1만큼 클때
            if check_cnt(arr, i, 0, flag) == False : return False
        elif arr[i]-1 == arr[i+1] :
            if check_cnt(arr, i, 1, flag) == False : return False
        else:
            return False
    return True

data, ans = [], 0
for _ in range(n) : data.append(list(map(int, input().split())))

for row in data: # row 검사
    if check_path(row) == True : ans += 1
for j in range(n): # col 검사
    col = []
    for i in range(n): col.append(data[i][j])
    if check_path(col) == True: ans +=1

print(ans)
# 이차원 배얄과 연산
# 1시간 16뷴

import copy

r, c, k = map(int, input().split())
r, c = r-1, c-1

data, t = [], 0
for _ in range(3): data.append(list(map(int, input().split())))

def R_sort(arr):
    max_len = -1e9
    new_arr = []

    for i in range(len(arr)):
        tmp, tmp_list = arr[i], []
        dict = {}
        for tp in tmp:
            if tp == 0 : continue
            if tp not in dict: dict[tp] = 1
            else : dict[tp] += 1
        for key in dict: tmp_list.append([key, dict[key]])
        tmp_list.sort(key = lambda x : (x[1], x[0])) 

        tpp = []
        for tp in tmp_list: tpp += tp
        max_len = max(len(tpp), max_len)
        new_arr.append(tpp)
        
    for i in range(len(new_arr)): new_arr[i] = new_arr[i] + [0]*(max_len - len(new_arr[i]))

    return new_arr

def C_sort(arr):
    max_len = -1e9
    c_list = []

    for j in range(len(arr[0])):
        tmp_list, dict = [], {}
        for i in range(len(arr)):
            target = arr[i][j]
            if target == 0 : continue
            if target not in dict : dict[target] = 1
            else : dict[target] +=1 
        for key in dict: tmp_list.append([key, dict[key]])
        tmp_list.sort(key = lambda x : (x[1], x[0])) 

        tpp = []
        for tp in tmp_list: tpp += tp
        max_len = max(len(tpp), max_len)
        c_list.append(tpp)

    for i in range(len(c_list)): 
        c_list[i] = c_list[i] + [0]*(max_len - len(c_list[i]))    
        if len(c_list[i]) > 100 : c_list[i] = c_list[0:100]
    
    new_arr = [[0 for _ in range(len(c_list))] for _ in range(len(c_list[0]))]

    for i in range(len(c_list)):
        for j in range(len(c_list[0])):
            new_arr[j][i] = c_list[i][j]

    return new_arr

arr = copy.deepcopy(data)
while True:
    if t > 100 : break    
    if r <= len(arr)-1 and c <= len(arr[0])-1 and arr[r][c] == k : 
        print(t)
        exit()
    
    new_arr = []
    if len(arr) >= len(arr[0]) : new_arr = R_sort(arr)    
    else : new_arr = C_sort(arr)
    
    arr = []
    arr = copy.deepcopy(new_arr)
    t += 1 

print(-1)

# 1. while True돌리면서 k+=1
# k > 100 이면 break
# 조건에 따라 2가지 연산이 존재한다.
# R연산 => 행 >= 열
# C연산 => 행 < 열 일때

# 연산시키면 [수 개수] => 이때 정렬시키면서 가장 큰 max_len알아두기.
# 정렬 끝난 후에는 max_len만큼 뒤에 0을 채우기.
# 행과 열의 길이가 100을 넘어가면 100뒤에는 버리기.


from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y, arr):
    q = deque()
    q.append((x, y))

    block = arr[x][y]
    blocks = [[x, y, block]]
    rainbow_blocks = []

    if block > 0:
        flag = True
    elif block == 0:
        flag = False
        rainbow_blocks.append([x, y])

    arr[x][y] = -2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0<=nx<n and 0<=ny<n): continue
            if arr[nx][ny] < 0: continue
            if arr[nx][ny] == 0 or arr[nx][ny] == block:
                if arr[nx][ny] > 0: flag = True
                if arr[nx][ny] == 0: rainbow_blocks.append([nx, ny])
                blocks.append([nx, ny, arr[nx][ny]])
                q.append((nx, ny))
                arr[nx][ny] = -2

    for x, y in rainbow_blocks: arr[x][y] = 0

    if len(blocks) >= 2 and flag:
        blocks.sort(key=lambda x : (-x[2], x[0], x[1]))
        return blocks
    return []

def find_largest_index(block_group):
    sorting_list = [[i] for i in range(len(block_group))]

    for i in range(len(block_group)):
        group = block_group[i]
        sorting_list[i].append(len(group))
        zero_cnt = 0
        for x, y, value in group:
            if value == 0: zero_cnt += 1
        sorting_list[i].append(zero_cnt)
        if group[0][2] != 0:
            sorting_list[i].append(group[0][0])
            sorting_list[i].append(group[0][1])
        else :
            sorting_list[i].append(-1)
            sorting_list[i].append(-1)

    sorted_list = sorted(sorting_list, key=lambda x : (-x[1], -x[2], -x[3], -x[4]))
    return sorted_list[0][0]


# 1. 얻었던 그룹의 길이의 제곱만큼 포인트 획득한다.
# 2. 블락을 없애고 새로운 배열을 return 한다.
def new_data(largest_group, data):
    global ans
    ans += len(largest_group)**2
    new_arr = [d[:] for d in data]
    for x, y, value in largest_group: new_arr[x][y] = -2
    return new_arr

# 1. tmp_list를 얻는다.
# 2. -2가 아닌 값들을 기록해둔다 + -1의 인덱스는 따로 기록해둔다.
# 3. 기록해둔 -1의 인덱스부터 거꾸로 기록을한다.
# 4. 기록해두는 곳은 이미 싹다 -2로 초기화 해둔 new_col에 하자.

# 이거 구현하는데 ㄹㅇ 한시간 소비한듯.
def grivated_data(new_data):

    grivated_arr = [[-2 for _ in range(n)] for _ in range(n)]
    tmp_arr = []
    for c in range(n):
        tmp_col = ['-1']
        index_list = [0]
        for r in range(n):
            block = new_data[r][c]
            tmp_col.append(str(block))
            if block == -1: index_list.append(r+1)
        tmp_col += ['-1']
        index_list.append(n+1)
        tmp_list = []
        for i in range(1, len(index_list)):
            start = index_list[i-1]+1
            end = index_list[i]+1
            space = tmp_col[start:end]
            leng = len(space)
            tmp_st = ''.join(space)
            tmp_st = tmp_st.replace('-2', '')
            tmp_st = tmp_st.replace('-1', 'B')
            tmp_st = (leng-len(tmp_st))*'X' + tmp_st
            tmp_list += tmp_st
        tmp_arr.append(tmp_list[:len(tmp_list)-1])

    for r in range(n):
        for c in range(n):
            block = tmp_arr[r][c]
            if block == 'X': grivated_arr[c][r] = -2
            elif block == 'B': grivated_arr[c][r] = -1
            else: grivated_arr[c][r] = int(block)

    return grivated_arr


def rotate(arr):
    tmp = [a[:] for a in arr]
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(3):
        for r in range(n):
            for c in range(n):
                ret[r][c] = tmp[n-c-1][r]
        tmp = [re[:] for re in ret]
    return ret

n, m = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))

ans = 0
arr = [d[:] for d in data]
while True:
#for _ in range(5):
    #print(ans)
    #for a in arr :print(a)
    #print()
    block_group = []
    for x in range(n):
        for y in range(n):
            if arr[x][y] < 0: continue
            group = bfs(x, y, arr)
            if not group: continue
            block_group.append(group)

    if len(block_group) == 0:
        #print('더이상 그룹 존재 x')
        break

    index = find_largest_index(block_group)
    largest_group = block_group[index]
    new_arr = new_data(largest_group, data)
    #print('제거')
    #for na in new_arr : print(na)
    grivated_arr = grivated_data(new_arr)
    #print('중력')
    #for na in grivated_arr : print(na)
    rotate_arr = rotate(grivated_arr)
    #print('회전')
    #for na in rotate_arr: print(na)
    rotate_grivated_data = grivated_data(rotate_arr)
    #print('다시 마지막 중력')
    #for na in rotate_grivated_data: print(na)

    data = [r[:] for r in rotate_grivated_data]
    arr = [d[:] for d in data]

print(ans)




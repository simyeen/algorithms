
n, t = map(int, input().split())
data, blizards = [], []
for _ in range(n): data.append(list(map(int, input().split())))
for _ in range(t): blizards.append(list(map(int, input().split())))

def sorted_bids(bids, data):
    global ans
    string = ''
    for x, y in bids:
        if data[x][y] == 0: continue
        string += str(data[x][y])

    if string == '': return ''

    while True:
        check_list = []
        st, tmp = string[0], [0]
        for i in range(1, len(string)):
            if st == string[i]:
                tmp.append(i)
            else:
                if len(tmp) >= 4: check_list.append(tmp)
                st = string[i]
                tmp = [i]
        if len(tmp) >= 4 : check_list.append(tmp)
        if len(check_list) == 0: return string

        # 4개 이상 중복 제거하면서 점수 계산하기.
        my_list = list(string)
        for check in check_list:
            ans += int(string[check[0]])*len(check)
            for k in check:
                my_list[k] = '0'

        sorted_string = ''.join(my_list)
        string = sorted_string.replace('0', '')
        if string == '' : return ''

def new_data(new_bids, bids):
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    string = new_bids

    st, tmp = string[0], [0]
    new_list, tmp_list = [], []

    for i in range(1, len(string)):
        if st == string[i]:
            tmp.append(i)
        else:
            new_list.append(len(tmp))
            new_list.append(int(string[tmp[0]]))
            st = string[i]
            tmp = [i]

    new_list.append(len(tmp))
    new_list.append(int(string[tmp[0]]))
    for i in range(len(new_list)):
        if i >= len(bids): break
        x, y = bids[i]
        new_arr[x][y] = int(new_list[i])
    return new_arr

bids = [[int(n/2), int(n/2)]]

i, end = 2, False
while True:
    if end == True: break
    x, y = bids[-1]
    for t in range(1, i):
        y -= 1
        bids.append([x, y])
        if [x, y] == [0, 0]:
            end = True
            break
    if end == True: break
    for t in range(1, i):
        x += 1
        bids.append([x, y])
    i += 1
    for t in range(1, i):
        y += 1
        bids.append([x, y])
    for t in range(1, i):
        x -= 1
        bids.append([x, y])
    i += 1

bids = bids[1:]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
ans = 0
for d, s in blizards:
    #1. 블리자드 마법 발사.
    x, y = int(n/2), int(n/2)
    d -= 1
    for i in range(1, s+1):
        nx, ny = x+direction[d][0]*i, y+direction[d][1]*i
        if not(0<=nx<n and 0<=ny<n): break
        data[nx][ny] = 0

    #2. 빈칸 채우고, 연속 제거하기
    new_bids = sorted_bids(bids, data)

    #3. 새로운 data_map 생성하기.
    if new_bids == '': break
    tmp_data = new_data(new_bids, bids)
    data = [t[:] for t in tmp_data]

print(ans)


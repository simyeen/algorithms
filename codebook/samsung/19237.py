
n, m, k = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))

sharks = [[i+1] for i in range(m+10)]
init_dir = list(map(int, input().split()))
for i in range(len(init_dir)): sharks[i].append(init_dir[i]-1)

s_dir = [[] for i in range(m+10)]
for i in range(m):
    for _ in range(4):
        a, b, c, d = map(int, input().split())
        s_dir[i].append((a-1, b-1, c-1, d-1))

move_table = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            ix, d = sharks[data[i][j] - 1]
            move_table[i][j].append(ix)
            move_table[i][j].append(d)
            move_table[i][j].append(k)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def minus_smell(moved_table):
    for i in range(n):
        for j in range(n):
            if len(moved_table[i][j]) == 2:
                if moved_table[i][j][1] == 1:
                    moved_table[i][j] = []
                else:
                    moved_table[i][j][1] -= 1


def next_d(x, y, ix, d, table):
    d_list = s_dir[ix-1][d]
    no_list = []
    for n_d in d_list:
        nx, ny = x+dx[n_d], y+dy[n_d]
        if not(0<=nx<n and 0<=ny<n): continue
        if len(table[nx][ny]) == 0: return n_d
        elif table[nx][ny][0] == ix:
            no_list.append(n_d)
    return no_list[0]

def move(next_move, table):
    # 충돌한 애들 제외시키고, 모두 이동시켜 준다.
    global cnt
    new_arr = [t[:] for t in table]

    dict = {}
    for next in next_move:
        nx, ny, ix, d = next
        key = str(nx) + str(ny)
        if key not in dict: dict[key] = [ix, d]
        elif dict[key][0] > ix: dict[key] = [ix, d]

    for before in next_move:
        x, y, ix, d = before
        new_arr[x-dx[d]][y-dy[d]] = [ix, k]

    for key in dict:
        nx, ny = key[0], key[1]
        ix, d = dict[key]
        new_arr[int(nx)][int(ny)] = [ix, d, k]

    return new_arr

def new_table(table):
    next_move = []
    # 다음 이동할 칸을 next_move에 담아준다.
    for x in range(n):
        for y in range(n):
            if len(table[x][y]) == 0: continue
            if len(table[x][y]) == 3:
                ix, d, k = table[x][y]
                new_d = next_d(x, y, ix, d, table)
                next_move.append([x+dx[new_d], y+dy[new_d], ix, new_d])

    return move(next_move, table)

def check_only_shark(table):
    check_cnt = 0
    for i in range(n):
        for j in range(n):
            if len(table[i][j]) == 3: check_cnt += 1
    if check_cnt == 1: return True
    else: return False

tmp_table = [m[:] for m in move_table]
cnt, t = 0, 0
while True:
    for d in tmp_table:print(d)
    print()
    if t >= 1000: break
    if check_only_shark(tmp_table) == True : break
    moved_table = new_table(tmp_table)
    minus_smell(moved_table)
    tmp_table = [m[:] for m in moved_table]
    t += 1

if t >= 1000: print(-1)
else: print(t)



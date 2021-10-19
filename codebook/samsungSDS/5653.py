dx = [-1,0,1,0]
dy = [0,1,0,-1]

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())

    data = []
    for _ in range(n): data.append(list(map(int, input().split())))

    dict = {}
    for x in range(n):
        for y in range(m):
            if data[x][y] == 0: continue
            value = data[x][y]
            key = str(x) + str(y)
            dict[key] = [x, y, value*2, value, True]

    for i in range(k):
        new_cell = {}
        for key in dict:
            if dict[key][2] == 0:
                dict[key][4] = False

        for key in dict:
            x, y, lifetime, value, is_alive = dict[key]
            if is_alive == False : continue # 이미, 죽은세포

            if lifetime == value: # 활성화 => 확장하기.
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    new_key = str(nx) + str(ny)
                    if new_key in dict: continue
                    if new_key not in new_cell:
                        new_cell[new_key] = [nx, ny, value*2, value, True]
                    else: # 추가하면서 중복될 때는 value로 비교하기.
                        if value > new_cell[new_key][1]:
                            new_cell[new_key] = [nx, ny, value*2, value, True]

            if lifetime > 0:
                dict[key] = [x, y, lifetime-1, value, True]

        for key in new_cell: dict[key] = new_cell[key]

    ans = 0
    for key in dict:
        if dict[key][2] != 0: ans += 1
    print(ans)


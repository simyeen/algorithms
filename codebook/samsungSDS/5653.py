from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

T = int(input())

for test_case in range(1, T+1):
    n, m, time = map(int, input().split())
    data = []
    for _ in range(n): data.append(list(map(int, input().split())))

    new_list = []
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                new_list.append((i, j, data[i][j]+1, data[i][j]))

    dead_list = []
    for t in range(time):
        q = deque()
        check_list = []
        for cell in new_list:
            x, y, life, value = cell
            q.append(cell)
            check_list.append((x, y))

        new_list = []
        print(q)
        for _ in range(len(q)):
            x, y, life, value = q.popleft()

            if life != 0:
                new_list.append([x, y, life-1, value])
                continue

            # life가 0이라 확장해야 될 때
            dead_list.append((x, y))
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                # 1. 이미 죽은애들이거나, 칸에 있던 애들 확장하지 않는다.
                if (nx, ny) in dead_list or (nx, ny) in check_list:
                    continue

                # 2. new_list에 넣어야 되는데 이미 존재해서 겹치는 값들이면?
                for cell in new_list:
                    c_x, c_y, c_life, c_value = cell
                    if (nx, ny) == (c_x, c_y): # 새로 확장하는 애들 겹친다면?
                        if value <= c_value : continue
                        new_list.remove(cell)
                        new_list.append([x,y,value+1, value])
                        break
                else : new_list.append([nx, ny, value+1, value])
        print('new_list', new_list)
        print(t, len(new_list))


# 1. 확장을 어떻게 할까?
# 2. 경계를 만나면 data의 범위를 2배로 기를까?
# 3. 그 다음에 기존 맵을 그 아에 옮겨?
# 4. 근데 그렇게 옮기게 되면 다시 새로운 좌표돌리면서 찾아야 될텐데...


# 1. 그냥 queue와 set, list로만 처리하는 건 어떨까?
# 2. q는 확장용만
# 3. (x, y, 현재 생존시간, 원래 자신이 가졌던 값)
# 4. 죽은애들을 따로넣는 dead_list를 두고 check를 할까?
# 5. q를 pop하면서 현재 생존시간이 0인 애들 => 데드리스트에 넣자.
# 6. 그리고 각 4방향으로 dead_list에 없으면


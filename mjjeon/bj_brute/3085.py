import sys

def countColor(in_list):
    c_cnt = [0, 0] # C, P, Z, Y
    p_cnt = [0, 0]
    z_cnt = [0, 0]
    y_cnt = [0, 0]

    for i in in_list:
        if i == 'C':
            c_cnt[0] += 1
            p_cnt[0] = 0
            z_cnt[0] = 0
            y_cnt[0] = 0
        elif i == 'P':
            p_cnt[0] += 1
            c_cnt[0] = 0
            z_cnt[0] = 0
            y_cnt[0] = 0
        elif i == 'Z':
            z_cnt[0] += 1
            c_cnt[0] = 0
            p_cnt[0] = 0
            y_cnt[0] = 0
        elif i == 'Y':
            y_cnt[0] += 1
            c_cnt[0] = 0
            p_cnt[0] = 0
            z_cnt[0] = 0
        
        c_cnt[1] = max(c_cnt)
        p_cnt[1] = max(p_cnt)
        z_cnt[1] = max(z_cnt)
        y_cnt[1] = max(y_cnt)

    return max(c_cnt[1], p_cnt[1], z_cnt[1], y_cnt[1])

N = int(sys.stdin.readline())
B = []
max_cnt = 0
D = [0 for _ in range(N)] * N

for i in range(N):
    B.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(N):
        # 이미 상, 좌 는 하, 우 를 하면 중복되는 거니까 하, 우 만 함.
        # 하    
        if i != N-1:
            # 바꾸기
            temp = B[i][j]
            B[i][j] = B[i+1][j]
            B[i+1][j] = temp
            # 갯수 세보기: 상하로 바꿨으니까 i(가로), i+1(가로), j열(세로)
            # i 번째 줄
            max_cnt = max(max_cnt, countColor(B[i]))
            # i + 1 번째 줄
            max_cnt = max(max_cnt, countColor(B[i+1]))
            # j 열
            max_cnt = max(max_cnt, countColor([B[k][j] for k in range(N)]))
            # 다시 바꾸기
            temp = B[i][j]
            B[i][j] = B[i+1][j]
            B[i+1][j] = temp
        # 우
        if j != N-1:
            temp = B[i][j]
            B[i][j] = B[i][j+1]
            B[i][j+1] = temp
            # 갯수 세보기: 좌우로 바꿨으니까 i(가로), j열(세로), j+1열(세로)
            # i 번째 줄
            max_cnt = max(max_cnt, countColor(B[i]))
            # j 열
            max_cnt = max(max_cnt, countColor([B[k][j] for k in range(N)]))
            # j 열
            max_cnt = max(max_cnt, countColor([B[k][j+1] for k in range(N)]))
            # 다시 바꾸기
            temp = B[i][j]
            B[i][j] = B[i][j+1]
            B[i][j+1] = temp


print(max_cnt)
import sys
N = int(sys.stdin.readline())
D = [[0,0,0] for i in range(N)]
result = 100000
input_list = []

for i in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))

for index in range(3):
    D[0] = [1000000, 1000000, 1000000]
    D[0][index] = input_list[0][index]
    
    for i in range(1, N):
        D[i][0] = min(D[i-1][1], D[i-1][2]) + input_list[i][0]
        D[i][1] = min(D[i-1][0], D[i-1][2]) + input_list[i][1]
        D[i][2] = min(D[i-1][0], D[i-1][1]) + input_list[i][2]

    for i in range(3):
        if i == index:
            continue
        result = min(result, D[N-1][i])

    # 틀렸습니다. -> 마지막 부분을 변수값에 저장하도록.. index에 해당하는 것은 안하고.
    # if index == 0:
    #     D[N-1][0] = 100000
    #     D[N-1][1] = min(D[N-1][0], D[N-1][2]) + input_list[N-1][1]
    #     D[N-1][2] = min(D[N-1][0], D[N-1][1]) + input_list[N-1][2]
    # elif index == 1:
    #     D[N-1][0] = min(D[N-1][1], D[N-1][2]) + input_list[N-1][0]
    #     D[N-1][1] = 100000
    #     D[N-1][2] = min(D[N-1][0], D[N-1][1]) + input_list[N-1][2]
    # elif index == 2:
    #     D[N-1][0] = min(D[N-1][1], D[N-1][2]) + input_list[N-1][0]
    #     D[N-1][1] = min(D[N-1][0], D[N-1][2]) + input_list[N-1][1]
    #     D[N-1][2] = 100000

    #print(D)


print(result)

# https://copy-driven-dev.tistory.com/m/78
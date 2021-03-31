# 테트로미노 종류
# 1: 0000
# 2: 00 
#    00
# 3: 0
#    0
#    00
# 4: 0
#    00
#     0
# 5: 000
#     0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


def find(x, y):
    global answer
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                next_x = x + tetromino[i][j][0] # x 좌표
                next_y = y + tetromino[i][j][1] # y 좌표
                result += board[next_x][next_y]
            except IndexError:
                continue
        answer = max(answer, result)
        
def solve():
    for i in range (n):
        for j in range(m):
            find(i, j)
            
answer = 0
solve()
print(answer)

# https://jeongchul.tistory.com/670 [Jeongchul]


# if 문으로 했는데 찾아보니까 저렇게 좌표 해놓고, index error 나면 그냥 exception 타게만 해놓으니까 편한듯..
# global 타입 변수로 함수 안에서도 공유함

# 틀렸습니다

# import sys

# N, M = map(int, sys.stdin.readline().split())
# T = []
# max_val = -1

# # 입력
# for i in range(N):
#     T.append(list(map(int, sys.stdin.readline().split())))

# for i in range(N):
#     for j in range(M):
#         # 1
#         if M-j >= 4:
#             max_val = max(max_val, T[i][j] + T[i][j+1] + T[i][j+2] + T[i][j+3]) # 1-1
#         if N-i >= 4:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+2][j] + T[i+3][j]) # 1-2
#         # 2
#         if N-i >= 2 and M-j >= 2:
#             max_val = max(max_val, T[i][j] + T[i][j+1] + T[i+1][j] + T[i+1][j+1]) # 2-1
#         # 3
#         if N-i >= 4 and M-j >= 2:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+2][j] + T[i+2][j+1] # 3-1
#                         , T[i][j] + T[i][j+1] + T[i+1][j+1]+ T[i+2][j+1] # 3-3
#                         , T[i][j] + T[i][j+1] + T[i+1][j] + T[i+2][j]) # 3-7
#         if M-j >= 3 and N-i >= 2:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i][j+1] + T[i][j+2] # 3-2
#                         , T[i][j] + T[i][j+1] + T[i][j+2] + T[i+1][j+2]) # 3-8
#         if M-j >= 3 and i >= 1 and N-i >= 2: 
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+1][j+1] + T[i+1][j+2]) # 3-6
#         if N-i >= 2 and j >= 2:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+1][j-1] + T[i+1][j-2]) # 3-4
#         if N-i >= 4 and j >= 1:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+2][j] + T[i+2][j-1]) # 3-5
#         # 4
#         if N-i >= 4 and M-j >= 2:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+1][j+1] + T[i+2][j+1]) # 4-1
#         if M-j >= 2 and j >= 1 and N-i >= 2:
#             max_val = max(max_val, T[i][j] + T[i][j+1] + T[i+1][j] + T[i+1][j-1]) # 4-2
#         if N-i >= 3 and j >= 1 and M-j >= 2:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+1][j-1] + T[i+2][j-1]) # 4-3
#         if N-i >= 2 and M-j >= 3:
#             max_val = max(max_val, T[i][j] + T[i][j+1] + T[i+1][j+1] + T[i+1][j+2]) # 4-4
#         # 5
#         if M-j >= 3 and N-i >= 2:
#             max_val = max(max_val, T[i][j] + T[i][j+1] + T[i+1][j+1] + T[i][j+2]) # 5-1
#         if N-i >= 4 and M-j >= 2:
#             max_val = max(max_val, T[i][j] + T[i+1][j] + T[i+2][j] + T[i+1][j+1]) # 5-2
#         if i >= 1 and M-j >= 3:
#             max_val = max(max_val, T[i][j] + T[i][j+1] + T[i][j+2] + T[i-1][j+1]) # 5-3
#         if i >= 1 and N-i >= 2 and M-j >= 2:
#             max_val = max(max_val, T[i][j] + T[i-1][j+1] + T[i][j+1] + T[i+1][j+1]) # 5-4


# print(max_val)
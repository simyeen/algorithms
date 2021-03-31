import sys
N = int(sys.stdin.readline())

for i in range(N):
    M, N, x, y = map(int, sys.stdin.readline().split())

    while x <= M*N:
        if x%N == y%N: # 같은표현: (x-y)%N == 0
            print(x)
            break
        x += M

    if x > M*N:
        print(-1)


# 시간초과
# def solution(M, N, x, y):
#     x_ = 0
#     y_ = 0
#     result = 0
#     while not (x_ == x and y_ == y):
#         x_ += 1
#         y_ += 1
#         result += 1
#         if x_ > M:
#             x_ = 1
#         if y_ > N:
#             y_ = 1

#         if result > 40000:
#             break
    
#     if result > 40000:
#         print(-1)
#     else:
#         print(result)

# N = int(sys.stdin.readline())

# for i in range(N):
#     M, N, x, y = map(int, sys.stdin.readline().split())

#     solution(M, N, x, y)

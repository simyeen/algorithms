N = int(input())
MAX = 30
D = [0] * (MAX + 1)
D[0] = 1
D[2] = 3
# D[4] = D[4-2] * 3 + D[4-4] * 2                  # 2칸 + 2칸 | 4칸 
# D[6] = D[6-2] * 3 + D[6-4] * 2 + D[6-6] * 2     # 4칸 + 2칸 | 2칸 + 4칸 | 6칸
# D[8] = D[8-2] * 3 + D[8-4] * 2 + D[8-6] * 2     # 6칸 + 2칸 | 4칸 + 4칸 | 6칸 + 2칸
# 규칙: -2 * 3이고, -4, -6, -8, ... 0 될 때까지는 *2 (2개의 경우만 나오니까.. *2, -4부터 시작이니까 i-4) 
#                   -> 이중 포문사용

for i in range(4, N + 1, 2):
    D[i] = D[i-2] * 3
    for j in range(i-4, -1, -2):
        D[i] += D[j] * 2

print(D[N])

# https://chldkato.tistory.com/118
# https://suri78.tistory.com/103

# 틀렸습니다

# N = int(input())
# MAX = 30
# D = [0] * (MAX + 1)
# D[2] = 3
# D[4] = D[2] ** (4/2) + 2
# for i in range(6, N + 1, 2):
#     D[i] = D[4] * (i-4) + D[6] * (i+1-6)

# print(D[N])

# 틀렸습니다

# N = int(input())
# MAX = 30
# D = [0] * (MAX + 1)
# D[2] = 3
# D[4] = 11
# for i in range(5, N + 1):
#     if i % 2 == 0:  # 짝수일 때
#         D[i] = 3**(i/2) + 2 * (i-4) * 3

# print(D[N])

# 틀렸습니다

# N = int(input())
# MAX = 30
# D = [0] * (MAX + 1)
# D[2] = 3
# D[4] = 11
# for i in range(5, N + 1):
#     if i % 2 == 0:  # 짝수일 때
#         D[i] = 3**(i/2) + 2 * D[i-4] # 2 * (i-4) * 3

# print(D[N])

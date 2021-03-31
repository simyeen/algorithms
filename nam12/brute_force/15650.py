# from itertools import permutations

# n, m = map(int, input().split())
# arr = []
# for i in range(1, n+1):
#     arr.append(i)

# check = False
# for c in permutations(arr, m):
#     check = False
#     for i in range(len(c)-1):
#         if int(c[i]) < int(c[i+1]):
#             check = True
#         else:
#             check = False
#             break
#     if(check):
#         print(" ".join(map(str, c)))

# 순열이랑 조합쓰면 좋을 줄 알았는데 index 구하기도 힘들고,
# 무조건 tuple로 반환되는거라 원소마다 형변환 비교해줘서 별로인듯.
# case가 클 땐 재귀로 돌리는 brute force가 제일 나은거 같다.(back tracking)
# N, M = map(int, input().split())

# num_list = [i + 1 for i in range(N)]
# check_list = [False] * N
# arr = []


# def dfs(cnt):
#     if(cnt == M):
#         print(*arr)
#         return

#     for i in range(0, N):
#         if(check_list[i]):
#             continue

#         check_list[i] = True
#         arr.append(num_list[i])
#         dfs(cnt + 1)
#         arr.pop()

#         for j in range(i + 1, N):
#             check_list[j] = False
#         # check_list[i] = False하면은 전부다 F가 되버려서 안됨.
# dfs(0)

from itertools import combinations

N, M = map(int, input().split())

c = combinations(range(1, N+1), M)
for i in c:
    print(' '.join(map(str, i)))

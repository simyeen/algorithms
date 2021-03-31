# N, M = map(int, input().split())
# num_list = list(map(int, input().split()))
# num = list(set(num_list))
# num.sort()
# n = len(num)

# check = [False for i in range(N)]
# ans = []


# def dfs(cnt):

#     if cnt == M:
#         print(*ans)
#         return

#     for i in range(n):

#         if (check[i]):
#             continue

#         check[i] = True
#         ans.append(num[i])
#         dfs(cnt+1)
#         ans.pop()
#         check[i] = False


# def dfs2(cnt):

#     if cnt == M:
#         print(*ans)
#         return

#     for i in range(n):

#         if (check[i]):
#             continue

#         ans.append(num[i])
#         dfs2(cnt+1)
#         check[i] = True
#         ans.pop()
#         check[i] = False


# if n > M:
#     dfs(0)
# else:
#     dfs2(0)

# N, M = map(int, input().split())
# num_list = list(map(int, input().split()))
# num = list(set(num_list))
# num.sort()
# n = len(num)

# check = [False for i in range(N)]
# ans = []


# def dfs(cnt):

#     if cnt == M:
#         print(ans)
#         return

#     else:
#         for i in range(n):

#             if (check[i]):
#                 continue

#             if n > M:
#                 check[i] = True
#             ans.append(num[i])
#             dfs(cnt+1)
#             if n < M:
#                 check[i] = True
#             ans.pop()
#             check[i] = False


# dfs(0)

from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list)  # 순서대로 나오게 정렬 먼저

arr = list(set(N_list))

output = []
for numbers in list(permutations(N_list, M)):
    output.append(numbers)
output = sorted(list(set(output)))  # 중복 제거 후 정렬 까지 한번에!

for numbers in output:
    for num in numbers:
        print(num, end=' ')
    print()

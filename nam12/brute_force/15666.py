
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

#     else:
#         for i in range(n):

#             if (check[i]):
#                 continue

#             ans.append(num[i])
#             dfs(cnt+1)
#             check[i] = True
#             ans.pop()
#             for j in range(i+1, N):
#                 check[j] = False


# dfs(0)

from itertools import combinations_with_replacement

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

output = []

for numbers in combinations_with_replacement(num_list, M):
    output.append(numbers)
output = list(sorted(set(output)))


for num in output:
    print(*num)

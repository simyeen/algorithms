# from itertools import product

# N, M = map(int, input().split())
# N_list = list(map(int, input().split()))
# N_list = sorted(N_list)  # 순서대로 나오게 정렬 먼저

# output = []
# for numbers in list(product(N_list, repeat=M)):
#     output.append(numbers)
# output = sorted(list(set(output)))  # 중복 제거 후 정렬 까지 한번에!


# for numbers in output:
#     print(*numbers)

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num = list(set(num_list))
num.sort()
n = len(num)

check = [False for i in range(N)]
ans = []


def dfs(cnt):

    if cnt == M:
        print(*ans)
        return

    else:
        for i in range(n):

            if (check[i]):
                continue

            ans.append(num[i])
            dfs(cnt+1)
            check[i] = True
            ans.pop()
            check[i] = False


dfs(0)

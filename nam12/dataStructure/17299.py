import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = [-1 for i in range(N)]
stack = []
F = [0 for _ in range(1000010)]

for i in range(len(arr)):
    F[arr[i]] += 1

for i in range(len(arr)):

    while stack and F[arr[stack[-1]]] < F[arr[i]]:
        ans[stack.pop()] = arr[i]

    stack.append(i)

for idx in ans:
    print(idx, end=" ")

# 왜 런타임 에러지 ????? 모르겟네.
# F부분의 초기화가 문제가 생김.
# dict를 사용해서 해볼 수 있다 key -> value.

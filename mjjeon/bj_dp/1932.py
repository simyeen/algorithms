import sys

# 입력
n = int(sys.stdin.readline())
d = [[0]*n for i in range(n)]
num = [0] * n
for i in range(n):
    num[i] = list(map(int, sys.stdin.readline().split()))

# dp
for i in range(n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = d[i-1][j] + num[i][j]
        elif j == i:
            d[i][j] = d[i-1][j-1] + num[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + num[i][j]

print(max(d[n-1]))

# https://m.blog.naver.com/PostView.nhn?blogId=occidere&logNo=220789773974&proxyReferer=https:%2F%2Fwww.google.com%2F
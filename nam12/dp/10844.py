import sys

num = int(sys.stdin.readline().rstrip())
mod = 1000000000

d = [[0]*10 for i in range(0, num+10)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, num+1):
    for j in range(10):
        if j == 0:
            d[i][j] = (d[i-1][j+1]) % mod
        elif j == 9:
            d[i][j] = (d[i-1][j-1]) % mod
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % mod

print(sum(d[num]) % mod)


# if j==0 if j== 9로 했었는데 멍청하게도
# 밑의 elif 안해주면 if j ==0 해준게 없어지게 되버림...

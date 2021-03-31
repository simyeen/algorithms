import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+10)

d[0], d[1] = 1, 1


for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 10007)

# 피보나치
# 계속 틀려서 보니깐 d[0]을 고려안해줬었음
# d[1], d[2] = 1,2 를 초기값으로 두고 돌렸던게 문제.

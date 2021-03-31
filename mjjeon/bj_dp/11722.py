import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
d_cnt = [1] * N

for i in range(N):
    for j in range(i):
        if p[i] < p[j] and d_cnt[i] < d_cnt[j] + 1:
            d_cnt[i] = d_cnt[j] + 1
                
print(max(d_cnt))
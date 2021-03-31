import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
d_cnt = [1] * N
d_cnt_r = [1] * N
# 원래 순서, 뒤집은 순서대로 하고
# 더해서 제일 큰 것 - 1
for i in range(N):
    for j in range(i):
        if p[i] > p[j] and d_cnt[i] < d_cnt[j] + 1:
            d_cnt[i] = d_cnt[j] + 1
        # if p[i] < p[j] and d_cnt_r[i] < d_cnt_r[j] + 1: # 틀렸습니다.
        #     d_cnt_r[i] = d_cnt_r[j] + 1
        # if p[N-1-i] > p[N-1-j] and d_cnt_r[i] < d_cnt_r[j] + 1: # 틀렸습니다.
        #     d_cnt_r[i] = d_cnt_r[j] + 1
        if p[N-1-i] > p[N-1-j] and d_cnt_r[N-1-i] < d_cnt_r[N-1-j] + 1:
            d_cnt_r[N-1-i] = d_cnt_r[N-1-j] + 1
            
for i in range(N):
    d_cnt[i] = d_cnt[i] + d_cnt_r[i]
print(max(d_cnt) - 1)

# https://sihyungyou.github.io/baekjoon-11054/
import sys
import copy

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
d_cnt = [1] * N
d = copy.deepcopy(p) 

for i in range(N):
    for j in range(i):
        if p[i] > p[j]:
            if d_cnt[i] < d_cnt[j] + 1:
                d[i] = max(d[j] + p[i], d[i]) # d[i] += p[j] --> d[i] = max(d[j] + p[i], d[i])
                d_cnt[i] = d_cnt[j] + 1
                
print(max(d))

# https://sihyungyou.github.io/baekjoon-11055/
# 틀렸습니다 

# import sys
# import copy

# N = int(sys.stdin.readline())
# p = list(map(int, sys.stdin.readline().split()))
# d_cnt = [1] * N
# d = p[:] # copy.deepcopy(p) #  
# # d = p 는 메모리가 같다
# # slicing 을 이용하면 shallow copy -> 해도 동작은 된다. p값 변경 시 d 도 변경되는데 p값을 안바꾸니깐..
# # deepcopy를 해야 deep copy (내부 객체까지 새롭게 copy) 가능
# # https://wikidocs.net/16038

# for i in range(N):
#     for j in range(i):
#         if p[i] > p[j]:
#             if d_cnt[i] < d_cnt[j] + 1:
#                 d[i] += p[j]
#             d_cnt[i] = max(d_cnt[i], d_cnt[j] + 1)
            
# print(max(d))

# +, -, 채널입력
# 채널 0에서 -누르면 그대로임.

# 목표 채널을 구하기 위해서
# 1. 주어진 배열의 수들을 len만큼 조합해서 모두 만들어보고
# 그 차이의 절댓값이 가장 작은 것을 고른다.
# 그리고 +, - 로 접근하기
# 2. +,- 로만 접근한 것이 채널이동 보다 작은지 확인해주기.

from itertools import product

cur = 100  # 시작 채널.
cnt = [0, 0]

goal = input()
leng = len(goal)
goal = int(goal)

n = int(input())
if (n > 0):
    remove_list = list(map(int, input().split()))
remocon_list = [i for i in range(10)]
for i in range(n):

    remocon_list.remove(remove_list[i])
cnt[0] = abs(goal - cur)  # +, -로만 이동하기.

flag = 600000

for i in range(1, leng+2):
    for c in product(remocon_list, repeat=i):  # 중복 순열 사용.

        temp = "".join(map(str, c))
        res = abs(goal-int(temp))

        if cnt[0] < res:
            continue
        if res < flag:
            flag = res
            cur = temp
cur = int(cur)
cnt[1] = len(str(cur)) + abs(goal-cur)

if cnt[0] > cnt[1]:
    print(cnt[1])
    exit()
else:
    print(cnt[0])

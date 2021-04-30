from itertools import combinations

n, m = map(int, input().split())
chiken, house = [], []

for r in range(n): # 입력과 동시에 위의 두 배열 초기화
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) 
        elif data[c] == 2:
            chiken.append((r, c))

candidates = list(combinations(chiken, m))

def get_sum(candidate):
    result = 0
    # 모든 집에 대해서 가장 가까운 치킨 거리 찾기.
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx-cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

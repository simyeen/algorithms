# 전체 치킨집 중에 M개를 고르자.
# 속하지 못한 치킨집은 0으로 초기화 하기.
# 도시의 치킨 거리는 모든 치킨거리의 합.

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
data, houses, chickens = [], [], []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1: houses.append((i, j))
        elif data[i][j] == 2: chickens.append((i, j))

def get_chicken_dist(house, chicken):
    x1, y1 = house
    x2, y2 = chicken
    return abs(x1-x2) + abs(y1-y2)

ans = 1e9
for combination in combinations(chickens, m):
    total_dist =[]
    for house in houses:
        tmp_dist = []
        for chicken in combination:
            tmp_dist.append(get_chicken_dist(house, chicken))
        total_dist.append(min(tmp_dist))
    ans = min(ans, sum(total_dist))

print(ans)
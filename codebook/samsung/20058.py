from itertools import combinations

n, m = map(int,input().split())

data = []
for _ in range(n): data.append(list(map(int, input().split())))

chickens, houses = [], []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 : houses.append((i,j))
        if data[i][j] == 2 : chickens.append((i,j))

combination = list(combinations(chickens, m))

ans = []
for combi in combination: # m개의 조합에 대해서 
    chicken_dist = []
    for house in houses: # 모든 house - chicken의 거리를 구하자.
        tmp = []
        for chicken in combi:
            dist = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]) 
            tmp.append(dist)
        chicken_dist.append(min(tmp))
    ans.append(sum(chicken_dist))

print(min(ans))
# 도시의 치킨 거리의 최솟값을 출력하자.
# 각 집에 대해서 치킨의 m개 만큼의 조합에 대한 거리를 모두 구하기
# 이때 한 집에 대해 치킨거리는 그 조합에 대해서 가장 작은 거리이다.
# 그 거리들의 합을 전부 구한 list를 만들어서 min값을 출력해내자
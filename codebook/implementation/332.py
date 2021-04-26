import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

houses = []
chickens = []
select_list = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))
select_list = list(combinations(chickens,m))

distance = [9999 for _ in range(len(houses))]

def get_distance(x, y):

    diff = x - y
    if diff < 0:
        return -diff
    else:
        return diff

for select in select_list:
    for i in range(len(select)):
        for j in range(len(houses)):
            target = get_distance(select[i][0], houses[j][0]) + get_distance(select[i][1], houses[j][1])
            if target < distance[j]:
                distance[j] = target
            print(distance)
print(sum(distance))





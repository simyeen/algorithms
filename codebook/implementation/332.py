import heapq
import sys
from itertools import combinations

# input = sys.stdin.readline().rstrip()

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

houses = []
chickens = []
distances = [[] for i in range(n+1)] 
answer = 0

for i in range (n):
    for j in range (n) :
        if arr[i][j] == 1: 
            houses.append((i,j))
        elif arr[i][j] == 2:
            chickens.append((i,j))

def get_distance():
    distance = 0
    for i in range (len(houses)):
        for j in range(len(chickens)):       
            distance = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])
            heapq.heappush(distances[i], (i, distance))
get_distance()

aa = list(combinations(distances, 2))
print(aa)

result = []
temp = 0
print(distances)
for _ in range(m):
    for i in range(len(houses)):
        now, distance = heapq.heappop(distances[i])
        temp += distance
        print(distance, temp)
    result.append(temp)

print(result)
print(min(result))

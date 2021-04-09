import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range (m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def solution(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

solution(start)

total = 0
time = 0
for d in distance :
    if d != INF and d != 0:
        total += 1
        time = max(time, d)

print(total, time)
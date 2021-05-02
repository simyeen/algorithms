import heapq
INF = 1e9

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijsktra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijsktra(graph, x, distance)

answer = []
for i in range(len(distance)):
    if k == distance[i]:
        answer.append(i)

if not answer:
    print(-1)
else :
    answer.sort()
    for i in answer:
        print(i)
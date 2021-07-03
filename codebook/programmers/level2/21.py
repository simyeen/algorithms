import heapq
INF = int(1e9)
n = 0 


def dij(start,graph,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        print(q)
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

def solution(N, road, K):
    
    start = 1
    graph = [[] for i in range(N+1)]
    distance = [INF] * (N+1)

    for i in road: # 양방향이라 2번 해줘야됨!
        a, b, c = i
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    dij(start,graph,distance)
    print(distance)

print(solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	,3))
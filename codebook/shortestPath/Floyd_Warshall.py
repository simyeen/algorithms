import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기.
n, e = map(int, input().split())
# 2차원 리스트(그래프)를 만들고, 모든 값을 무한으로 초기화한다.
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기자신으로 가능 경로는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1): 
        if a == b :
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력하기.
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("도달할 수 없음.", end=' ')
        else :
            print(graph[a][b], end=' ')
    print()


graph = [
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

visited = [False]*9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor_v in graph[v] :
        if not visited[neighbor_v] :
            dfs(graph, neighbor_v ,visited)




dfs(graph, 1, visited)
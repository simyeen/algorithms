from collections import deque
import copy

v = int(input())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]
time = [0]*(v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i) # x -> i임 진입차수니까

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], time[i] + result[now])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,v+1):
        print(result[i])
topology_sort()

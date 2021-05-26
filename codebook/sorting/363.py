import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

answer = []
while q:
    first =  heapq.heappop(q)

    if q: 
        second = heapq.heappop(q)
        temp = first + second
        answer.append(temp)
        heapq.heappush(q,temp)

print(sum(answer))

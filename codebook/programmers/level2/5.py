import heapq

def solution(scoville, K):
    answer = 0
    
    q = []
    for i in scoville :
        heapq.heappush(q, i)
    
    while True:
        print(q)
        if len(q) == 1 : return -1 

        if q and q[0] >= K : return answer

        if q and len(q) >= 2: 
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            heapq.heappush(q,(first + second*2))
            answer += 1


print(solution([1, 2, 3, 9, 10, 12], 7))
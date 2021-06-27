import heapq

def solution(scoville, K):
    answer = 0
    
    q = []
    for i in scoville :
        heapq.heappush(q, i)
    
    while True:
        if not q or (len(q) == 1 and q[0] < K) : return -1 

        if q and q[0] >= K : return answer

        if q and len(q) >= 2: 
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            heapq.heappush(q,(first + second*2))
            answer += 1

import heapq

def solution(people, limit):
    answer = 1
    q = []
    
    for i in people:
        heapq.heappush(q, i)
    
    rest = limit
    while q :
        print(q)
        peo = heapq.heappop(q)
        print(rest)
        rest -= peo
        print(rest)
        if rest >= 0:
            continue
        elif rest < 0 :
            heapq.heappush(q, peo)
            rest = limit 
            answer += 1
        
    return answer

people = [70, 50, 80, 50]	
limit = 100

print(solution(people,100))
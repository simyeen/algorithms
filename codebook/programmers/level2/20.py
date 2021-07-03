from collections import deque

def solution(people, limit):
    ans = 0
    q = deque(sorted(people))

    while q :
        left = q.popleft()
        if not q :
            return ans +1 
        right = q.pop()
        if left + right > limit:
            deque.appendleft(left)
        ans += 1
    return ans


people = [70, 50, 80, 50]	
limit = 100

print(solution(people,100))
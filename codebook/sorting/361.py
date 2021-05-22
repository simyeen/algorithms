N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
        # 1 / 2 2 2 / 3 3 / 4 / 6

def solution(N, stages):
    answer = []
    count = [0] * 100
    total = len(stages)
    stages.sort()
    last = stages[-1]

    for i in stages:
        count[i] += 1

    for i in range(1, last+1):
        if i == N+1:
            break
        fail =  count[i] / total
        answer.append((i,fail))
        total -= count[i]
    answer = sorted(answer, key = lambda x : x[1], reverse=True)
    
    answer = [i[0] for i in answer]
    return answer

print(solution(N, stages))
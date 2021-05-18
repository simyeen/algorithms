N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	

def solution(N, stages):

    answer = []
    result = []
    total = len(stages)
    count = [0] * 10

    stages.sort()
    for i in stages:
        count[i] += 1

    for i in range(1, stages[-1]+1):
        if i == N+1:
            break
        result.append((i, count[i]/total))
        total -= count[i]

    result.sort(key = lambda x : -x[1])    
    for ans in result:
        answer.append(ans[0])
    return answer

print(solution(N, stages))
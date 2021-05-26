N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
        # 1 / 2 2 2 / 3 3 / 4 / 6


# 이 방식으로 하면 테케 통과 못하는데 왜그런지 모르겠음.
def solution(N, stages):
    answer = []
    count = [0] * 100
    length = len(stages)

    for i in stages:
        count[i] += 1

    for i in range(1, N+1):
        print(count[i])

        if length == 0:
            fail = 0
        else : 
            fail =  count[i] / length

        answer.append((i,fail))
        length -= count[i]
        
    answer = sorted(answer, key = lambda x : x[1], reverse=True)
    
    answer = [i[0] for i in answer]
    return answer

print(solution(N, stages))
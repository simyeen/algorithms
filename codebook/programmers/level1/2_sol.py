def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else: #else문을 for문과 같은 줄에 쓰게되면, for문의 반복이 끝나고나서 else문이 실행되게 된다. (break로 빠져나가지 않는다면) for else문 !
            answer += 1

    return answer
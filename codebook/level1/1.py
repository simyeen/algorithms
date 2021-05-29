
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...


answers = [1,3,2,4,2]
count = [0]*4

def solution(answers):
    answer = []
    target1 = [1, 2, 3, 4, 5]
    target2 = [2, 1, 2, 3, 2, 4, 2, 5]
    target3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        index1 = i % len(target1)
        index2 = i % len(target2)
        index3 = i % len(target3)

        if answers[i] == target1[index1]:
            count[1] += 1
        if answers[i] == target2[index2]:
            count[2] += 1
        if answers[i] == target3[index3]:
            count[3] += 1
    max_value = max(count)
    for i in range(1,4):
        if count[i] == max_value:
            answer.append(i)

    return answer

print(solution(answers))
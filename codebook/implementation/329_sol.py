
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥인 경우
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer :
                continue
            return False
        elif stuff == 1:
            if [x, y-1, 0]1 in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
        return True
1
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operator = frame
        if operator == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operator == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)



def solution(name):
    answer = 0

    target = ['A' for _ in name]

    right, left, up, down = 0, 0, 0, 0

    i = 0
    for char in name :
        c = ord(char)
        t = ord(target[i])
        
        if c != t and i == 0: # 제일 처음 시작할 때
            up = 


    return answer


print(solution("JEROEN"))

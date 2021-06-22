def solution(s):
    target = s.split()
    print(target)

    answer = []
    for char in target:
        print("char", char)
        tmp = ""
        for j in range(len(char)):
            print("j", j, char[j])
            if j % 2 == 0:
                tmp += char[j].upper()
            else : tmp += char[j].lower()
            print("tmp", tmp)
        answer.append(tmp)

    return " ".join(answer)
    

print(solution("try hello world"))
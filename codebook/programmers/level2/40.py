dict = {
    "A" : 1,"B" : 2,"C" : 3,"D" : 4,"E" : 5,"F" : 6, "G" : 7,
    "H" : 8,"I" : 9,"J" : 10,"K" : 11, "L" : 12,
    "M" : 13, "N":14, "O":15, "P":16, "Q":17, "R":18, 
    "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26
}

def solution(msg):
    answer = []
    i, cnt = 0, 27

    while True:
        if i == len(msg) - 1: # 등록하고 다시 돌아왔을 때 끝난다.
            answer.append(dict[msg[i]])
            return answer
        j = i 
        tmp = msg[j]
        while True : # 계속 ok하다가 끝난다.
            if tmp in dict: # 계속 존재해서 다음꺼 확인하기.
                j += 1
                if j == len(msg): # 계속 ok되다가 끝나버릴 때
                    answer.append(dict[tmp])
                    return answer
                tmp += msg[j]
            else : # tmp에서 가장 마지막 글자만 빼고 answer에 추가하기.
                dict[tmp] = cnt
                answer.append(dict[tmp[:-1]])
                i = j
                cnt += 1     
                break      
            
msg = 'ABABABABABABABAB'
print(solution(msg))
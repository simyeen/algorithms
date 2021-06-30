

def solution(name):
    answer = 0
    
    cur = ord('A')
    for i in range(len(name)):
        
        target = ord(name[i])-26 if ord(name[i]) > 90 else ord(name[i])

        up = abs(target - cur) 
        if cur == 'A':
            down = min(abs(target-cur), abs(target-ord('Z'))+1)
        else : down = up
        left = abs(target-ord('A'))+1
        right = abs(target-ord('Z'))+1
        
        print(up,down,left,right)
        answer += min(up,down,right,left)
        print(answer, name[i])
        cur = ord(name[i])
    return answer


print(solution("JEROEN"))

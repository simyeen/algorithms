def solution(name):
    answer = 0
    
    cur = ord('A')
    stack = []
    for i in range(1,len(name)):
        target = [ord(name[i])-26 if name[i] > 90 else ord(name[i])]
        
        up = abs(target - cur) # 업, 다운으로 만
        if cur == 'A':
            down = min(abs(target-cur), abs(target-ord('Z')+1))
        left = abs(target-ord('A')+1)
        right = abs(target-ord('Z')+1)
        
        answer += min(up(min(down(min(left,right)))))
        
        cur = name[i]
    return answer
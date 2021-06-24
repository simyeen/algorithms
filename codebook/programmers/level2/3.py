def solution(record):
    answer = []
    dic = {}
    for cmds in record:
        cmds = cmds.split(' ')
        if cmds[0] != 'Leave' :
            dic[cmds[1]] = cmds[2]
    
    for cmds in record:
        cmds = cmds.split(' ')
        if cmds[0] == 'Enter':
            answer.append(dic[cmds[1]] + '님이 들어왔습니다.')
        elif cmds[0] == 'Leave':
            answer.append(dic[cmds[1]] + '님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
def solution(info, query):
    answer = []
    inf, que = [], []

    for i, q in zip(info, query):
        inf.append(i.split(' '))
        q = q.replace(' and ', ' ')
        que.append(q.split(' '))
        
    print(inf[0], que[0])
    for qu in que: # 5가지 조건을 가진 쿼리 하나에 대하여
        cnt = 0
        for io in inf: # 주어진 info 5개를 전부 비교한다.
            for i in range(len(qu)): #qu의 조건 하나하나를 비교한다.
                if i == (len(qu)-1) and int(io[i]) >= int(qu[i]): # 마지막 점수에 대하여
                    cnt += 1
                    break
                if qu[i] == '-' : continue
                if qu[i] != io[i] : break
        answer.append(cnt)
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
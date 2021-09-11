import re

def solution(info, query):
    inf, que, que_leng = [], [], []
    for i, q in zip(info,query):
        inf.append(i.split())
        q = q.replace(' and', '')
        q = q.replace('-', '')
        que_leng.append(len(q.split()))
        que.append(q.replace(' ',''))
    
    ans = [0 for _ in range(len(que))]
    for infos in inf: 
        info_reg = '|'.join(infos[:len(infos)-1])+'|\d+' 
        score = infos[-1]
        p = re.compile(f'{info_reg}')
        for j in range(len(que)):
            filtered_query = p.findall(que[j])
            if que_leng[j] == len(filtered_query):
                if int(score) >= int(filtered_query[-1]): ans[j] += 1
    return ans

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

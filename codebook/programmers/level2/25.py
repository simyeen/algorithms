from itertools import combinations

def solution(relation):
    answer = 0
    cur = 1 
    record = [i for i in range(len(relation[0]))]
    n = len(relation)
    check_set = set()
    
    while cur <= len(record): 
        
        combination = list(combinations(record,cur)) # 1에서 최대 n까지의 조합이다.
        tmp_list = []
        for combi in combination: # 4C2 같은 조합 중에 하나    
            
            tmp = ''
            for c in combi: tmp += str(c)
            for check in check_set: # 최소성 검사
                if check in tmp: break
            
            else :  
                cmp_set = set()
                for i in range(n):
                    tmp = ''
                    for c in combi: # 1, 2 전부다 더해주기
                        tmp += str(relation[i][c])
                    cmp_set.add(tmp)

                if len(cmp_set) == n : # 중복없으므로 키 값으로 인정된다.
                    tmp = ''
                    for c in combi: tmp += str(c)
                    tmp_list.append(tmp) # 해당 cur일때  
                    answer += 1
        for check in tmp_list: check_set.add(check)
        cur += 1
    
    return answer

relations = [["100","ryan","music","2"],["200","apeach","math","4"],["300","tube","computer","3"],["400","con","computer","1"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]
print(solution(relation))


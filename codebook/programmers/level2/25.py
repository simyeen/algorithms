from itertools import combinations

def solution(relation):
    answer = 0
    cur = 1 
    record = [i for i in range(len(relation[0]))]
    n = len(relation)
    check_list = []
    
    while cur <= len(record): 
        
        combination = list(combinations(record,cur)) # 1에서 최대 n까지의 조합이다.

        for combi in combination: # 4C2 같은 조합 중에 하나    
            for c in combi : # 이미 키인 열인지 검사
                if c in check_list: 
                    break
            else :  
                cmp_set = set()
                for i in range(n):
                    tmp = ''
                    for c in combi: # 1, 2 전부다 더해주기
                        tmp += relation[i][c]
                    cmp_set.add(tmp)
                if len(cmp_set) == n : # 중복없으므로 키 값으로 인정된다.
                    for c in combi:
                        check_list.append(c)
                    answer += 1
                            
        cur += 1
    
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","1"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))


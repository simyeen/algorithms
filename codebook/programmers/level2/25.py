from itertools import combinations

def check_minimal(combi,check_list): # combi의 04 => 013, 014, 045 

    for check in check_list : # check가 하나라도 combi안에 존재할때 아웃
        cnt = len(check)
        for c in check:
            if c in combi: cnt -= 1
        if cnt == 0 : return False
    return True

def solution(relation):
    answer = 0
    n = len(relation)
    check_list = []

    for i in range(1,len(relation[0])+1):
        combination = list(combinations(range(len(relation[0])),i))
        for combi in combination:
            if check_minimal(combi,check_list) == False: continue
            tmp_set = set()
            for i in range(len(relation)):
                tmp = ''
                for c in combi: # 0, 1, 2 3개다 같은 곳에 담아줘야함.
                    tmp += relation[i][c] # r[0][0] + [0][1] + [0][2]
                tmp_set.add(tmp)
            if len(tmp_set) == n: # combi가 하나의 키값이 될 때
                check_list.append(combi)
                answer += 1

    return answer

relations = [["100","ryan","music","2"],["200","apeach","math","4"],["300","tube","computer","3"],["400","con","computer","1"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]
print(solution(relation))


from itertools import combinations

def check_min(test, combi): # 최소성 => 이미 check된 열이 있는 조합은 건너뛴다.
    for te in test :
        cnt = 0
        for t in te:
            if t in combi : cnt+=1
        if cnt == len(te) :return False
    return True

def check_unique(check_set, n): # unique하게 key로 사용할 수 있는지 검사한다.
    if len(check_set) == n : return True
    return False

def solution(relation):
    n, m = len(relation), len(relation[0]) # 행과 열
    check_list = [False for _ in range(m)]
    test = []
    
    ans = []
    for i in range(1, m+1): # 1개에서 m개 까지 고른다.
        arr = [i for i in range(m)] # m=4이면 0~3까지의 뽑자.
        combination = list(combinations(arr, i)) # 조합을 생성 
        
        for combi in combination : # 1개, 2개, 3개 ... m개의 조합까지.
            if check_min(test, combi) == False : continue # 한 조합내애서 이미 어떤 원소가 check인지 아닌지 판별한다.
            check_set = set()
            for r in range(n): # 행에 대해서
                tmp = []
                for c in combi: # combi에 존재하는 열에 대해서    
                    tmp.append(str(relation[r][c])) #tmp에 1+2이런식을 만들어서 아래 set에 넣고 중복성 판단하기.
                #print(tmp, combi, check_list)
                check_set.add(' '.join(tmp))
            print(check_set)

            if check_unique(check_set, n) == False: continue # 다 만들어진 check_set에 대해서 길이가 행과 같은지 판단.
            #for c in combi : check_list[c] = True # 유일성이 인정된 열들은 check해주기.
            print(combi)
            test.append(combi)
    print(test)
    return len(test)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]


relations = [
    ['a','1','4'],
    ['2','1','5'],
    ['a','2','4'],]

print(solution(relations))
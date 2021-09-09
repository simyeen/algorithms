from itertools import combinations

def check_min(ans, combi): # 최소성 => 이미 check된 열이 있는 조합은 건너뛴다.
    for min_key in ans :
        cnt = 0
        for key in min_key:
            if key in combi : cnt+=1
        if cnt == len(min_key) :return False
    return True

def check_unique(check_set, n): # unique하게 key로 사용할 수 있는지 검사한다.
    if len(check_set) == n : return True
    return False

def solution(relation):
    n, m = len(relation), len(relation[0]) # 행과 열
    
    ans = []    
    for i in range(1, m+1): # 1개에서 m개 까지 고른다.
        arr = [i for i in range(m)] # m=4이면 0~3까지의 뽑자.
        combination = list(combinations(arr, i)) # 조합을 생성 
        
        for combi in combination : 
            if check_min(ans, combi) == False : continue 
            check_set = set()
            for r in range(n): 
                tmp = []
                for c in combi: tmp.append(str(relation[r][c])) 
                check_set.add(' '.join(tmp))

            if check_unique(check_set, n) == False: continue 
            ans.append(combi)
    print(ans)
    return len(ans)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]


relations = [
    ['a','1','4'],
    ['2','1','5'],
    ['a','2','4'],]

print(solution(relations))
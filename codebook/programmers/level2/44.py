from itertools import combinations

def solution(orders, course):

    dict = {}
    for order in orders :
        for c in course :
            if len(order) < c: break 
            tmp = [st for st in order]
            combination = list(combinations(tmp,c))
            for combi in combination:    
                string = ''.join(combi)
                st = [s for s in string]
                st.sort()
                st = ''.join(st)
                if st not in dict: dict[st] = 1
                else : dict[st] += 1
    
    result = [[] for _ in range(11)]
    for key in dict:
        result[len(key)].append((key, dict[key]))
    
    ans = []
    for c in course:
        if len(result[c]) == 0: continue
        tmp_list = sorted(result[c], key = lambda x : -int(x[1]))
        max_value = tmp_list[0][1]
        if max_value ==1 : continue
        ans.append(tmp_list[0][0])
        for t in tmp_list[1:] : 
            if max_value != t[1]: break
            ans.append(t[0])
    
    return sorted(ans)
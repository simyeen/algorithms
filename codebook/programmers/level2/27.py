from itertools import combinations

def solution(orders, course):
    answer = []

    dict = {}
    for i in orders:
        for c in i :
            dict[c] = True
        
    for i in course:
        mylist = list(combinations(dict, i)) # i만큼의 조합 
        
        tmp = []
        max_value = -1e9

        for per in mylist: # i만큼의 조합중에서 하나에 대해
            cnt = 0
            for order in orders: # orders에 몇개나 있는지 cnt
                for p in per:
                    if p not in order: break
                else : cnt += 1
            if cnt < 2 : continue
            max_value = max(cnt, max_value)
            tmp.append((per,cnt))
        for k in tmp:
            if max_value == k[1]:
                ans = sorted(k[0])
                answer.append("".join(ans))

    return sorted(answer)


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,4]

print(solution(orders, course))
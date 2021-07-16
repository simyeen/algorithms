from itertools import combinations

def solution(number, k):
    answer = ''

    combi = list(combinations(number, len(number)-k))
    mylist = []

    for c in combi:
        tmp = ''
        for i in c :
            tmp += i
        mylist.append(int(tmp))
    answer = str(max(mylist))

    return answer

print(solution('1924',2))

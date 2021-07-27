from itertools import combinations, permutations

n = int(input())

data = []
for _ in range(n): data.append(list(map(int,input().split())))

combination = list(combinations(range(n),n//2))
combination = combination[:len(combination)//2]

ans = []
for team in combination: 
    total_team = set(range(n))
    rest_team = total_team - set(team)
    
    per1 = list(permutations(team, 2))
    per2 = list(permutations(rest_team, 2))

    tmp = 0
    for p in per1: tmp += data[p[0]][p[1]]
    for p in per2 : tmp -= data[p[0]][p[1]]
    ans.append(abs(tmp))

print(min(ans))




n = int(input())

houses = list(map(int, input().split()))
count = [0] * 200010

for i in houses:
    count[i] += 1

house_set = set(houses) # 중복 제거 및 sort가능.

result = 1e9
answer = houses[0]

for antena in house_set:
    total = 0
    for house in house_set:
        total += (abs(antena - house)) * count[house]
    
    if result > total :
        result = total
        answer = antena
        
print(answer)
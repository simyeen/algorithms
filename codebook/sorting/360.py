n = int(input())

house = list(map(int, input().split()))
house.sort()

start = house[0]
last = house[-1]

min_value = 1e9
answer = start

for i in range(start, last+1):
    result = 0
    for h in house :
        result += abs(h-i)

    if min_value > result :
        min_value = result
        answer = i

print(answer)
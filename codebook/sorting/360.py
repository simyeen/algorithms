n = int(input())

house = list(map(int, input().split()))
house.sort()

count = []

start = house[0]
last = house[-1]

for i in house:
    count[i] += 1

min_value = 1e9
answer = start

ho = set(house)
for i in range(start, last+1):
    result = 0
    for h in ho :
        result += abs(h-i)*count[ho]

    if min_value > result :
        min_value = result
        answer = i

print(answer)
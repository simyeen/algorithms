n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range (1, sum(arr)):
    now = i
    for x in arr :
        if now - x in arr :
            break
        
print(now)
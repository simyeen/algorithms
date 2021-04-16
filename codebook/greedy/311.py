
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
team = []*(n+1)

cnt = 0
for i in range(len(data)):
    
    now = data[-1]
    while now:
        data.pop()
        now -= 1
    cnt += 1    

print(cnt)
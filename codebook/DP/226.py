n, m  = map(int, input().split())

d = [-1]*(m+1)
arr = []

for i in range(n):
    arr.append(int(input()))
    d[arr[i]] = 1    

for i in range(1, m+1):
    temp = []

    for j in arr:
        if d[i] == -1 and i > j:
            temp.append(d[i-j]) 
    print(temp)
    d[i] = min(temp)+1
    

print(arr, d)
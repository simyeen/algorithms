n, m  = map(int, input().split())

d = [-1]*(m+2)
arr = []

for i in range(n):
    arr.append(int(input()))
    d[arr[i]] = 1    

for i in range(arr[0], m+1):
    if i in arr :
        continue
    min_value = 9999
    for j in arr :
        if d[i-j] != -1 :
          min_value = min(min_value, d[i-j])+1
    d[i] = min_value
    
print(d[m])




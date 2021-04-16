data = input()

arr = [0]*2

first = int(data[0])

for i in range(1, len(data)):
    if i == len(data):
        arr[first] += 1

    if first == int(data[i]):
        continue
    else :
        arr[first] += 1
        first = int(data[i])
        
print(arr)    

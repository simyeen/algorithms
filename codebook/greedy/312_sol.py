data = input()

result = int(data[0])
for i in data[1:]: # same that using range(1, len(data)) but you have to access num = int(data[i]) 
    now = int(i)
    if result <= 1 or now <= 1:
        result += now
    else :
        result *= now
print(result)
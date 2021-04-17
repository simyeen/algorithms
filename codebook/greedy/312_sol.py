data = input()

result = int(data[0])
for i in data[1:]:
    now = int(i)
    if result <= 1 or now <= 1:
        result += now
    else :
        result *= now
print(result)
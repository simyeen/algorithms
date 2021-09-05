n = int(input())
arr = list(map(int, input().split()))
b, c = map(int,input().split())

people1 = 0
people2 = 0

data = []
for person in arr:
    tmp = 0
    if person <= b:
        continue
    person -= b

    if person < c : tmp = 1
    elif person % c == 0 : tmp = person//c
    else : tmp = int(person//c)+1
    data.append(tmp)

print(len(arr) + sum(data))


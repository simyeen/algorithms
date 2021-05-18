n = int(input())
data = []

for _ in range(n):
    data.append(list(input().split()))
    # list빼도 똑같이 들어가넹!

data.sort(key = lambda x : ( -int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(data[i][0])
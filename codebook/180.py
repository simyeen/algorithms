n = int(input())

arr = []
for i in range(n) :
    arr.append(input().split())

def setting(data):
    return int(data[1])

result = sorted(arr, key = setting)

# ans = []
# for i in range(n) :
#     ans.append(result[i][0])
# print(*ans)


for string in result : 
    print(string[0], end= " ")
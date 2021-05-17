n = int(input())
answer = []
data = []

for i in range(n):
    a, b, c, d = list(input().split())
    b, c, d = map(int, (b, c, d))
    data.append([a,b,c,d])

left = []
right = []

def sorting(arr, k):
    if not arr:
        return print("종료")

    arr.sort(key=lambda x : x[k])
    
    while data:
        

    sorting(k+1)
    
    print("i")

    sorting(k+1)

sorting(data, 1)
    


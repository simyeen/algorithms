# 게리멘더링2 => 2시간 15분...

from itertools import product

n = int(input())
data = []
for _ in range(n) : data.append(list(map(int, input().split())))

d1_list = [i+1 for i in range(int(n/2))]
d2_list = [i+1 for i in range(int(n/2))]
d_combination = list(product(d1_list, d2_list))

ans = []
for combination in d_combination:
    d1, d2 = combination
    five_list = []
    for i in range(n):
        for j in range(n):
            if 0<= i + d1 + d2 <= n-1:
                if 0<= j-d1 < j and j < j+d2 <= n-1 : five_list.append((i,j))
    
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for x,y in five_list:
        edges = set()

        for i in range(d1+1): edges.add((x+i,y-i))
        for i in range(d2+1): edges.add((x+i,y+i))
        for i in range(d2+1): edges.add((x+d1+i,y-d1+i))
        for i in range(d1+1): edges.add((x+d2+i,y+d2-i))

        flag = False
        for i in range(n):
            for j in range(n):
                if (i,j) == (x,y) or (i,j) == (x+d1+d2, y+d2-d1):
                    arr[i][j] = 5
                    continue
                if (i,j) in edges :
                    if flag == False: flag = True                        
                    else : flag = False
                    arr[i][j] = 5
                    continue
                if flag == True : 
                    arr[i][j] = 5
                    continue
        
                if 0<=i<x+d1 and 0<=j<=y : arr[i][j] = 1
                elif 0<=i<=x+d2 and y<j<=n-1 : arr[i][j] = 2
                elif x+d1<=i<=n-1 and 0<=j<y-d1+d2 : arr[i][j] = 3
                elif x+d2<i<=n-1 and y-d1+d2<=j<=n-1 : arr[i][j] = 4

        tmp_list = [0 for _ in range(6)]
        for i in range(n):
            for j in range(n):
                tmp_list[arr[i][j]] += data[i][j]
        
        tmp_list = tmp_list[1:]
        ans.append(max(tmp_list) - min(tmp_list))

print(min(ans))


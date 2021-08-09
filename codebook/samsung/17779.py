from itertools import product
import copy

n = int(input())
data = []
for _ in range(n) : data.append(list(map(int,input().split())))

# x,y,d1,d2를 어떻게 정할까?

point_list = [i for i in range(n)]
d_list = [i for i in range(1,n)]

products = list(product(point_list,point_list,d_list,d_list))

combinations = []
for pro in products:
    x,y,d1,d2 = pro 
    if x < x+d1+d2 <= n-1 :
        if 0 <= y-d1 < y and y < y+d2 <= n-1:
            combinations.append(pro)

def count():pass
    
for combi in combinations:
    x,y,d1,d2 = combi
    
    state_data = [[0 for _ in range(n)] for _ in range(n)]
    state_data[x][y] = 6
    state_data[x+d1][y-d1] = 7
    state_data[x+d2][y+d2] = 7
    state_data[x+d2+d1][y+d2-d1]=7

    print('전')
    for i in state_data : print(i)
    print()

    for r in range(n):
        for c in range(n):
            if 0 <= r < x+d1-1 and 0<= c <= y : state_data[r][c] = 1
            elif 0 <= r <= x+d2 and y-1 < c <= n-1 : state_data[r][c] = 2
            elif x+d1-1 <= r <= n-1 and 0 <= c < y-d1+d2: state_data[r][c] = 3
            elif x+d2 < r <= n-1 and y-d1+d2-1 <= c <= n-1: state_data[r][c] = 4

    state_data[x][y] = 5
    state_data[x+d1][y-d1] = 5
    state_data[x+d2][y+d2] = 5
    state_data[x+d2+d1][y+d2-d1]=5
    print('후')
    for i in state_data:
        print(i)
    print()


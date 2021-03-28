# n = int(input())

# arr = list(input().split())

# goal = [1, 1]

# for i in range (len(arr)) :
    
#     if arr[i] == 'L' :
#         if(goal[1]==1):
#             continue
#         else:
#             goal[1]-=1
#             continue
#     elif arr[i] == 'R' :
#         if(goal[1] == n):
#             continue
#         else : 
#             goal[1] +=1 
#             continue
#     elif arr[i] == 'U' :
#         if(goal[0] == 1):
#             continue
#         else : 
#             goal[0] +=1
#             continue
#     elif arr[i] == 'D' :
#         if(goal[0] == n):
#             continue
#         else : 
#             goal[0] +=1
            

# print(*goal)


# 개선해야 할 점 : 단순히 goal[0,1] 및 +-1로 접근하는 것 보다 좌표적인 개념을 도입해서 구현하자.

n = int(input())

x, y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range (len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue
    x, y = nx, ny

print(x,y)

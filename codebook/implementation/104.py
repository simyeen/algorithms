n = int(input())

arr = list(input().split())

goal = [1, 1]

for i in range (len(arr)) :
    
    if arr[i] == 'L' :
        if(goal[1]==1):
            continue
        else:
            goal[1]-=1
            continue
    elif arr[i] == 'R' :
        if(goal[1] == 5):
            continue
        else : 
            goal[1] +=1 
            continue
    elif arr[i] == 'U' :
        if(goal[0] == 1):
            continue
        else : 
            goal[0] +=1
            continue
    elif arr[i] == 'D' :
        if(goal[0] == 5):
            continue
        else :
            goal[0] +=1
            

print(*goal)
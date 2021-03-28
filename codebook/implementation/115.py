#8가지 경우의 수로 이동할 수 있다.

start = input()

x = ord(start[0])
y = int(start[1])

paths =  [(-2,1),(-2,-1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)]

cnt = 0
for path in paths : 
    
    if ord('a') > x + path[0] or ord('h') < x + path[0] :
        continue
    if 1 > y +path[1] or 8 < y + path[1] :
        continue
    cnt+=1

print(cnt)           
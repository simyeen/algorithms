from collections import deque

# 회전한 톱니바퀴와 맞닿은 극이 다르면 
# 회전하기 전에 톱니바퀴의 극을 확인 하고 회전 시킬 바퀴들을 정한다.

RIGHT_INDEX = 2
LEFT_INDEX = 6

wheels = []
for _ in range(4): wheels.append(deque(input()))
n = int(input())

cmds = []
for _ in range(n) : cmds.append(list(map(int, input().split())))

def rotate(rotate_lists):

    for rotat in rotate_lists:
        i, d = rotat
        target = wheels[i]
        if d == 1 : target.appendleft(target.pop()) # 시계방향 회전
        else : target.append(target.popleft())
        

for cmd in cmds:
    index, direction = cmd[0]-1, cmd[1]
    target = wheels[index]
    LEFT, RIGHT = target[LEFT_INDEX], target[RIGHT_INDEX]

    rotate_lists = [(index,direction)]
    d = direction
    for left in range(index-1,-1,-1):
        if wheels[left][RIGHT_INDEX] == LEFT : break 
        else : 
            d =  -d    
            rotate_lists.append((left,d))
            LEFT = wheels[left][LEFT_INDEX]
    d = direction
    for right in range(index+1,len(wheels)):
        if wheels[right][LEFT_INDEX] == RIGHT : break 
        else : 
            d =  -d    
            rotate_lists.append((right,d))
            RIGHT = wheels[right][RIGHT_INDEX]
    rotate(rotate_lists)

score = 0
if wheels[0][0] == '1' : score += 1
if wheels[1][0] == '1' : score += 2
if wheels[2][0] == '1' : score += 4
if wheels[3][0] == '1' : score += 8

print(score)

    


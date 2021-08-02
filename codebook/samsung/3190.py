from collections import deque

wheels = []
RIGHT_INDEX = 2
LEFT_INDEX = 6


for _ in range(4):
    tmp = list(input())
    wheels.append(deque(tmp))

n = int(input())
cmds = []
for _ in range(n): cmds.append(list(map(int, input().split())))

# 시계방향 =>
# 반시계방향 => 
for cmd in cmds:
    index, direction = cmd[0]-1, cmd[1]
    target = wheels[cmd[0]-1] # 명령어 따라서 회전 시키기
    if direction == 1: target.appendleft((target.pop())) #시계방향
    else : target.append(target.popleft()) # 반시계방향

    left, right = target[LEFT_INDEX], target[RIGHT_INDEX]

    left_d = -1 if direction == 1 else 1
    for i in range(index-1,-1,-1): # 왼쪽 톱니 바퀴들 회전시키기.
        left_wheel = wheels[i]
        if left_wheel[RIGHT_INDEX] == left : break # 같은 극일 때
        else : # 다른 극 일때 반대 방향으로 회전하기
            if left_d == -1 : left_wheel.append(left_wheel.popleft())
            else : left_wheel.appendleft((left_wheel.pop()))
            left = left_wheel[LEFT_INDEX] # 새로운 left로 갱신해주기
            left_d = left_d = -1 if left_d == 1 else 1

    right_d = -1 if direction == 1 else 1
    for i in range(index+1,len(wheels)): # 오른쪽 톱니 바퀴들 회전시키기.
        right_wheel = wheels[i]
        if right_wheel[LEFT_INDEX] == right : break
        else : # 다른 극 일때 반대 방향으로 회전하기
            if right_d == -1 : right_wheel.append(right_wheel.popleft())
            else : right_wheel.appendleft((right_wheel.pop()))
            right = right_wheel[RIGHT_INDEX] # 새
            right_d = right_d = -1 if right_d == 1 else 1

    for w in wheels:
        print(w)
    print()

score = 0
if wheels[0][0] == '1' : score += 1
if wheels[1][0] == '1' : score += 2
if wheels[2][0] == '1' : score += 4
if wheels[3][0] == '1' : score += 8
print(score)








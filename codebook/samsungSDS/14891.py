from collections import deque

wheels = [deque() for _ in range(4)]
for i in range(4):
    st = input()
    for s in st:
        wheels[i].append(int(s))

k = int(input())
cmds = []
for _ in range(k): cmds.append(list(map(int, input().split())))

LEFT, RIGHT = 6, 2

def rotate(wheels, index, d):
    if d == 1:
        wheels[index].appendleft(wheels[index].pop())
    else:
        wheels[index].append(wheels[index].popleft())

def search(start, d):
    rotate_list = [[False, -1] for _ in range(4)]
    rotate_list[start] = [True, d]

    left_d, right_d = d, d
    for i in range(start, 4): # 오른쪽 탐색
        if i == 3 or wheels[i][RIGHT] == wheels[i+1][LEFT]: break
        right_d = (right_d + 1) % 2
        rotate_list[i+1] = [True, right_d]

    for i in range(start, 0, -1): # 왼쪽 탐색
        if i == 0 or wheels[i][LEFT] == wheels[i-1][RIGHT]: break
        left_d = (left_d + 1) % 2
        rotate_list[i-1] = [True, left_d]

    return rotate_list

for start, d in cmds:
    start -= 1
    if d == -1 : d = 0

    rotate_list = search(start, d)
    for i in range(len(rotate_list)):
        flag, dir = rotate_list[i]
        if flag:
            rotate(wheels, i, dir)

ans = 0
for i in range(len(wheels)):
    ans += wheels[i][0] * (2**i)
print(ans)

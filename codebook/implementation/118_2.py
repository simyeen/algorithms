def turn_left():
    return (direction+3) % 4

row, col = map(int, input().split())

r, c, direction = map(int, input().split())
d = [[0]*col for i in range(row)]
d[r][c] = 1

arr = []
for i in range (row):
    arr.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

turn_time = 0
cnt = 0
while True:
    turn_left()
    nr = r + dr[direction]
    nc = c + dc[direction]

    if arr[nr][nc] == 0 and d[nr][nc] == 0:
        d[nr][nc] = 1
        r = nr
        c = nc
        cnt += 1
        turn_time = 0
    else :
        turn_time += 1
        if turn_time == 4:
            if d[nr][nc] == 1:
                break
            else:
                r = r + dr[(direction+2)%4]
                c = c + dc[((direction+2)%4)]
                turn_time = 0

print(cnt)

# def turn_left():
#     return (direction+3) % 4

# row, col = map(int, input().split())

# r, c, direction = map(int, input().split())
# d = [[0]*col for i in range(row)]
# d[r][c] = 1

# arr = []
# for i in range (row):
#     arr.append(list(map(int, input().split())))

# dr = [-1, 0, 1, 0]
# dc = [0, -1, 0, 1]

# turn_time = 0
# cnt = 0
# while True:
#     turn_left()
#     nr = r + dr[direction]
#     nc = c + dc[direction]

#     if arr[nr][nc] == 0 and d[nr][nc] == 0:
#         d[nr][nc] = 1
#         r = nr
#         c = nc
#         cnt += 1
#         turn_time = 0
#     else :
#         turn_time += 1
#         if turn_time == 4:
#             if d[nr][nc] == 1:
#                 break
#             else:
#                 r = r + dr[(direction+2)%4]
#                 c = c + dc[((direction+2)%4)]
#                 turn_time = 0

# print(cnt)






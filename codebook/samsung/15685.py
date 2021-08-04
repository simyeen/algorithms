data = [[0 for i in range(101)] for _ in range(101)]

directions = [(1,0),(0,-1),(-1,0),(0,1)]

n = int(input())
cmds = []
for _ in range(n): cmds.append(list(map(int, input().split())))


def rotate(dragon, g): 
    
    for _ in range(g):
        core = dragon[-1]



def extend(): pass

def check() : pass

for cmd in cmds:
    x, y, d, g = cmd
    dx,dy = directions[d]
    nx, ny = x + dx, y + dy

    dragon = []
    dragon.append((x,y))
    if 0 <= nx <= 100 and 0 <= ny <= 100 : dragon.append((nx,ny))

    rotate(dragon, g)


# x,y 와 d를 가지고 일단 선분 하나 0세대 짜리를 만든다.
# 그다음에 g를 보고 시계방향으로 90도 회전 시킨 애를 tmp에 저장시킨다.
# 기존의 드래곤 커브와 회전시켜서 추가 된 드래곤 커브를 이어붙인다.
# 마지막에 check 함수를 통해서 검사하기




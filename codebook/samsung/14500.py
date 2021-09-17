n, m = map(int, input().split())

data = []
for _ in range(n) : data.append(list(map(int, input().split())))

max_value = -1e9

x, y = 0,0
tetris = [

    [
        [[0,y] for y in range(4)], # ----
        [[x,0] for x in range(4)]  # 세로
    ]

    ,[
        [[x,y],[x,y+1],[x+1,y],[x+1,y+1]]
    ]

    ,[
        [[x,y],[x+1,y],[x+2,y],[x+2,y+1]],
        [[x,y],[x+1,y],[x,y+1],[x,y+2]],
        [[x,y],[x,y+1],[x+1,y+1],[x+2,y+1]],
        [[x+1,y],[x+1,y+1],[x+1,y+2],[x,y+2]],

        [[x,y+1],[x+1,y+1],[x+2,y+1],[x+2,y]],
        [[x,y],[x+1,y],[x+1,y+1],[x+1,y+2]],
        [[x,y],[x,y+1],[x+1,y],[x+2,y]],
        [[x,y],[x,y+1],[x,y+2],[x+1,y+2]],
    ]

    ,[
        [[x,y],[x+1,y],[x+1,y+1],[x+2,y+1]],
        [[x+1,y],[x+1,y+1],[x,y+1],[x,y+2]],
        [[x,y+1],[x+1,y],[x+1,y+1],[x+2,y]],
        [[x,y],[x,y+1],[x+1,y+1],[x+1,y+2]],
    ]

    ,[
        [[x,y],[x,y+1],[x,y+2],[x+1,y+1]],
        [[x+1,y],[x,y+1],[x+1,y+1],[x+2,y+1]],
        [[x,y+1],[x+1,y],[x+1,y+1],[x+1,y+2]],
        [[x,y],[x+1,y],[x+2,y],[x+1,y+1]],
    ]
]

def check(lego) : 
    for x, y in lego:
        if x < 0 or x >= n or y < 0 or y >= m : return False
    return True

for arr in tetris:
    for item in arr:
        for i in range(n):
            for j in range(m):
                lego = [[it[0]+i,it[1]+j] for it in item]                
                if check(lego) == False : continue
                tmp = 0
                for x, y in lego: tmp += data[x][y]
                max_value = max(max_value, tmp)

print(max_value)

        

n,M,k = map(int,input().split())

fireball = []
for _ in range(M): 
    x,y,m,s,d = map(int,input().split())
    fireball.append((x-1,y-1,m,s,d,False))

data = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for ball in fireball:
    x, y = ball[0], ball[1]
    data[x][y].append(ball)

def sum_div():  
    for row in data:
        for col in row:
            if len(col) == 0 : continue
            if len(col) == 1 : 
                x,y,m,s,d,check = col.pop()
                data[x][y].append((x,y,m,s,d,False))
                continue
            sum_m, sum_s, sum_d, leng = 0, 0, [], len(col)
            while col:
                x,y,m,s,d,check = col.pop()
                sum_m += m
                sum_s += s
                sum_d.append(d)
            m, s= int(sum_m/5), int(sum_s/leng)
            if m == 0 : continue

            d_check = 0
            for d in sum_d:
                if d % 2 == 0 : d_check += 1 # 짝수이면 +
                else : d_check -= 1 # 홀수이면 - 
        
            if d_check == 4 or d_check == -4 :
                for d in range(0,7,2):
                    data[x][y].append((x,y,m,s,d,False))
            else :
                for d in range(1,8,2):
                    data[x][y].append((x,y,m,s,d,False))

for _ in range(k):    
    for row in data: # 이동시키기
        for col in row:
            if len(col) <= 0: continue
            for _ in range(len(col)):
                x,y,m,s,d,check = col.pop()
                if check == True: 
                    col.insert(0,(x,y,m,s,d,check))
                    continue
                nx = (x + dx[d]*s)%(n) 
                ny = (y + dy[d]*s)%(n)
                data[nx][ny].insert(0,(nx,ny,m,s,d,True))    
    sum_div()

ans = 0
for row in data:
    for col in row:
        if len(col) == 0: continue
        while col:
            x,y,m,s,d,check = col.pop()
            ans += m
print(ans)


# 파이어 볼 초기화 nxn행렬에
# k번 만큼 실행
# stack에 m개의 파이어 볼 정보 저장.
# 0,1는 위치 2는 질량 3는 속력(이동 칸 수) 4는 방향


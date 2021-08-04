import copy

n, m, k = map(int, input().split())

start = []
for _ in range(m) : 
    x,y,m,s,d = map(int,input().split())
    start.append(list((x-1,y-1,m,s,d)))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def spread_balls(tmp_list,fireballs):
    
    for i in range(n):
        for j in range(n):
            if len(tmp_list[i][j]) == 0 : continue
            if len(tmp_list[i][j]) == 1 : 
                fireballs.append(tmp_list[i][j][0])
                continue
        
            sum_m, sum_s, check_dlist = 0, 0, []
            for ball in tmp_list[i][j]:
                x,y,m,s,d = ball
                sum_m += m
                sum_s += s
                check_dlist.append(d)

            sum_m, sum_s = int(sum_m/5), int(sum_s/len(tmp_list[i][j]))
            if sum_m == 0 : continue # 소멸
            
            check_d = 0
            for check in check_dlist: 
                if check % 2 == 0 : check_d += 1
                else : check_d -= 1
            
            if abs(check_d) == len(check_dlist):
                for d in range(0,7,2):
                    fireballs.append((x,y,sum_m,sum_s,d))
            else : 
                for d in range(1,8,2):
                    fireballs.append((x,y,sum_m,sum_s,d))

fireballs = copy.deepcopy(start)
for _ in range(k): # k번의 명령 실행
    tmp_list = [ [[] for _ in range(n)] for _ in range(n)]
    while fireballs: # 파이이볼 이동시키기
        x,y,m,s,d = fireballs.pop()
        nx, ny = (x + dx[d]*s)%n, (y + dy[d]*s)%n
        tmp_list[nx][ny].append((nx,ny,m,s,d))    

    spread_balls(tmp_list,fireballs) #파이어 볼 2개 이상 합치기

ans = 0 
for ball in fireballs:
    x,y,m,s,d = ball
    ans += m

print(ans)

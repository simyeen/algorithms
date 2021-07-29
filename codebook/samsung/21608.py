n = int(input())

input_data = []
for _ in range((n**2)): input_data.append(list(map(int, input().split()))) # 초기화 

dx = [-1,0,1,0]
dy = [0,1,0,-1]

data = [[0 for _ in range(n)] for _ in range(n)]

def check_node(node) : # data를 돌면서 빈 노드를 대상으로 인접한 학생 등 파악
    target = node[0] 
    friends = [f for f in node[1:]]

    tmp = []
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 : continue # 넣을 수 없는 칸 이니깐
            x, y = i, j
            cnt, zero = 0, 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or n <= nx or ny < 0 or n <= ny: continue #범위 밖일 때
                if data[nx][ny] in friends : cnt+=1 
                elif data[nx][ny] == 0 : zero += 1
            tmp.append((cnt,zero,i,j))
    tmp.sort(key=lambda x : (-(x[0]), -(x[1]) , x[2], x[3]))
    x, y = tmp[0][2],tmp[0][3]
    data[x][y] = target


def cal(data, input_data) : # 돌면서 만족도 계산하기.
    sum_value = 0
    score = [0,1,10,100,1000]
    for i in range(n):
        for j in range(n):
            cnt = 0
            for node in input_data:
                if node[0] == data[i][j]:
                    x,y = i,j
                    friends = [f for f in node[1:]]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
                        if data[nx][ny] in friends : cnt+=1
            sum_value += score[cnt]
    return sum_value

for node in input_data:
    check_node(node)

ans = cal(data, input_data)
print(ans)


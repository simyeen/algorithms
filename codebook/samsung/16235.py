# 나무 재태크
# 시간 초과 발생.
# 해쉬로 접급하는 건 빠르다. 그런데 사실 N=10이라서 그냥 for_for로 돌려도 전혀 무관했었다.
# heapq때문에 timeout이 발생한듯 => 가을에서 삽입마다 nlogn이 발생하기 때문.
# 진짜 빠르게 하고 싶으면 deque로 해서 어차피 나무가 느는 방법은 가을 뿐 이니깐, 그냥 앞에 삽입해주면 
# 봄에서도 굳이 정렬안해줘도 된다.



import heapq

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

n, m, k = map(int, input().split())

energes = [[5 for _ in range(n)] for _ in range(n)]

A = []
for _ in range(n): A.append(list(map(int,input().split())))

trees = dict()
for _ in range(m) : 
    x, y, c = map(int, input().split())
    x, y = str(x-1), str(y-1)
    key = ''.join(x+y)
    if key not in trees: 
        trees[key] = [c]
        heapq.heapify(trees[key])
    else : heapq.heappush(trees[key],c)

for _ in range(k):
    # 1. 봄 + 여름 
    for key in trees:
        tree = trees[key]
        if len(tree) == 0 : continue

        x, y = int(key[0]), int(key[1])
        spring_list, summer = [], 0
        while tree:
            age = heapq.heappop(tree)
            if age <= energes[x][y]:
                energes[x][y] -= age
                spring_list.append(age+1)
            else : summer += int(age/2)
        energes[x][y] += summer
        for tmp in spring_list: heapq.heappush(tree, tmp)
        
    # 가을에 번식한다.    
    new_trees = dict()
    for key in trees : new_trees[key] = trees[key]

    for key in trees:
        tree = new_trees[key]
        if len(tree) == 0 : continue
        for i in range(len(tree)):
            if tree[i] % 5 != 0: continue
            x, y = int(key[0]), int(key[1])
            for j in range(8): # 5의 배수면 증식시킨다.
                nx, ny = x + dx[j], y + dy[j]
                if not (0<=nx<n and 0<=ny<n): continue
                new_key = ''.join(str(nx)+str(ny))
                if new_key not in new_trees:
                    new_trees[new_key] = [1]
                    heapq.heapify(new_trees[new_key])
                else : heapq.heappush(new_trees[new_key],1)
    trees = dict()
    for key in new_trees: trees[key] = new_trees[key]

    for i in range(n):
        for j in range(n):
            energes[i][j] += A[i][j]
    
ans = 0
for key in trees : ans += len(trees[key])
print(ans)
            


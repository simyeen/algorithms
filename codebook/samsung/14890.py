n, l = map(int, input().split())

data = []
for _ in range(n): data.append(list(map(int, input().split())))

# 행 순으로 돌기
ans = 0

for i in range(n):
    j = 0
    while j < n-l:
        target1, cnt = data[i][j], 0
        target2 = data[i][j+1]
        check = False

        if abs(target1-target2) >= 2 : break
        for k in range(l-1):
            if target2 != data[i][j+k] : 
                check = True
                break



        j += l


    print()

# 열 순으로 돌기
for j in range(n):
    for i in range(n):
        pass


# 경사로를 어떤 순으로 놓을까?
# 행 / 열 순서로 놓기
# 행에서도 왼 / 오 이렇게 2번 돌릴까?
# 가다가 높은 애 만나면 이전꺼 L개 확인하기
# 가다가 낮은 애 만나면 다음꺼 L개 확인하기

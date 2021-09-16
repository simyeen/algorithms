# 마법사 상어와 파이어스톰

# L만큼 격자나누기
# 모든 부분의 격자를 시계방향으로 90도 회전시키기.

n, q = map(int, input().split())
data = []
for _ in range(2**n): data.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))

for L in cmds:
    e = 2**L
    
    for i in range(0, 2**n, e):
        pass
    print()
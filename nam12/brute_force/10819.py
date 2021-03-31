from itertools import permutations

N = int(input())
a = list(map(int, input().split()))
m = -1
for number in permutations(a, N):
    tmp = 0
    for i in range(0, len(a)-1):
        tmp += abs(number[i] - number[i+1])
    if m < tmp:
        m = tmp
print(m)

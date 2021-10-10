from itertools import permutations

n = int(input())
k = int(input())

arr = []
for _ in range(n) : arr.append(int(input()))

permutation = list(permutations(arr, k))


ans = set()
for per in permutation:
    tmp = ''
    for p in per : tmp += str(p)
    ans.add(int(tmp))

print(len(ans))



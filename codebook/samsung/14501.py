n = int(input())

t, p = [], []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


arr = []
for i in range(n):
    sum_value = 0
    while True:
        sum_value += p[i]
        i = i + t[i] 
        if i >= n : break
    arr.append(sum_value)
print(arr)
#  1  =>   4     =>    5
#  i => i + t[i] => i+t[i] + t[i + t[i]]
# p[i] + p[i+t[i]] + 
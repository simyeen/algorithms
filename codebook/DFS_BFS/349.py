from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
temp = []

for i in range(len(operators)):
    if operators[i] > 0 :
        for _ in range(operators[i]):
            temp.append(i)

operator = list(permutations(temp, n-1))

min_value = 1e9
max_value = -1e9

def get_operator(a, op, b):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 3:
        return int(a/b)
    elif op == 2:
        return a * b

for op in operator:
    result = 0
    result = get_operator(numbers[0], op[0], numbers[1])
    for i in range(1, len(op)):
        result = get_operator(result, op[i], numbers[i+1])

    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)

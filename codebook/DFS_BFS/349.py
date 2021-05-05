n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

for op in operators:
    if op > 0 :
        

min_value = 1e9
max_value = -1e9

result = 0


for number in numbers:
    

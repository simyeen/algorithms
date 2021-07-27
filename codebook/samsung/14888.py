from itertools import permutations
from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))

op = []
for _ in range((oper[0])): op.append('+')
for _ in range((oper[1])): op.append('-')
for _ in range((oper[2])): op.append('*')
for _ in range((oper[3])): op.append('/')

permutation = list(set(permutations(op,n-1)))


def operating(a,op,b):
    if op == '*' : return a*b
    elif op == '+' : return a+b
    elif op == '-' : return a-b
    elif op == '/':
        if a < 0 and b > 0: return -(-a//b)
        return a//b

ans = []
for per in permutation:
    expression = deque()
    for num, op in zip(numbers, per): 
        expression.append(num)
        expression.append(op)
    expression.append(numbers[-1])
    
    while len(expression) != 3:
        tmp = operating(expression.popleft(),expression.popleft(),expression.popleft() )
        expression.appendleft(tmp)
    ans.append(operating(expression.popleft(),expression.popleft(),expression.popleft()))

max_value, min_value = max(ans), min(ans)

print(max_value)
print(min_value)



# oper에 따른 만큼 연산자 경우의 수 구하기
# 순열한다음에 set으로 하면 될 듯
from itertools import permutations
import re

def operating(a,op,b):
    a, b = int(a), int(b)
    if op == '*' : return str(a*b)
    elif op == '+' : return str(a+b)
    else : return str(a-b)

def solution(expression):
        
    permutation = list(permutations(('*','+','-'),3))
    
    p = re.compile('\d+|\D')
    express = p.findall(expression)
    ans = []
    for operator in permutation: # 각 우선수위마다
        exp = express
        for op in operator: # * -> + -> - 이럴 떄
            while True:
                if op in exp:
                    i = exp.index(op)
                    tmp = [operating(exp[i-1],exp[i],exp[i+1])]
                    if len(exp) == 3:
                        exp = tmp
                        break
                    if i == 1 and len(exp) > 3: # 가장 앞의 연산일 때
                        exp = (tmp) + exp[i+2:]
                    elif i == len(exp)-2: # 가장 뒤의 연산일 때
                        exp = exp[:i-1] + (tmp)
                    else : exp = exp[:i-1] + tmp + exp[i+2:]
                    continue
                break
        
        ans.append(abs(int(exp[0])))

    return max(ans)
print(solution("100-200*300-500+20"))
        
        
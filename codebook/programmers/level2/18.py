from collections import deque

def solution(s):
    answer = 0
    q = deque()
    for i in s:
        q.append(i)
    
    stack = []
    for i in range(len(s)):
        q.append(q.popleft()) # 한 번 회전시킴
        
        for i in q: # 회전 시킨 s에 대해서
            if i == '[' or i == '(' or i =='{': # 여는 괄호 스택에 넣기.
                stack.append(i)
            elif i == ']': 
                if stack[-1:] == ['[']:
                    stack.pop()
                else : break
                    
            elif i == ')': 
                if stack[-1:] == ['(']:
                    stack.pop()
                else : break
                    
            elif i == '}': 
                if stack[-1:] == ['{']:
                    stack.pop()
                else : break
        else :
            if len(stack) == 0 : answer += 1
    
    return answer

s = "[](){}"
print(solution(s))
def check(string):
    temp = []
    
    for i in range(len(string)):
        pass


def solution(p):
    if p == '':
        return ''
    if check(p):
        

    u = []
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
            u.append('(')

        elif p[i] == ')':
            count -= 1
            u.append(')')
    
    return answer

p = input()

print(solution(p))
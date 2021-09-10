# 괄호 변환

def check_balanced(p): 
    if p == '' : return -1
    
    cur = p[0]
    cnt = 1
    for i in range(1, len(p)):
        st = p[i]
        if cur == st: cnt +=1
        else : cnt -= 1
        if cnt == 0 : return i+1

def check_right(u) : 
    if u[0] == ')' : return False
    stack = ['(']

    for st in u[1:]:
        if len(st) == 0 : return False # 도중에 스택이 다 비면 종료.
        if st == '(' : stack.append('(')
        else : stack.pop() 
    if len(stack) == 0 : return True # 마지막 검사.

def solution(p):

    u_list = []
    while True:
        if check_balanced(p) < 0 : break
        else : index = check_balanced(p)
        u = p[:index]
        u_list.append(u)
        p = p.replace(u, '', 1)
    
    check_list = [False for _ in range(len(u_list))]
    for i in range(len(u_list)): check_list[i] = check_right(u_list[i])

    print(u_list)
    ans = ''
    for i in range(len(u_list)-1, -1, -1):
        print(ans)
        u = u_list[i]
        if check_list[i] == True: ans = u + ans # ans가 
        else :
            reverse_u = [st for st in u]
            reverse_u.pop()
            reverse_u.pop(0)
            if len(reverse_u) != 0 : 
                for j in range(len(reverse_u)):
                    if reverse_u[j] == '(' : reverse_u[j] = ')'
                    else : reverse_u[j] = '('
            ans = '(' + ans + ')' + ''.join(reverse_u)
    return ans



p = '()))((()'
print(solution(p))

# 1. u를 본다 => u, v로 나눈다. => check_balanced()
# => 일단 u, v로 나누자!
# 2. u가 올바른지 확인하자. check_right()

# 3. 올바르면 answer = u + v하고 v에 대해서 다시 실행하기.
# 4. 올바르지 않다면 answer = ( v최종본 ) + 뒤집은u
# 5. 이제 다시 v를 u로 넣고 실행


# => 1u 2u 3u 4u 5u 6u 공란 이렇게하면 안되나?
# => 뒤에서 부터 보면서 6u가 올바르면? ans = u + ''
# => 5u가 올바르면? ans = 5u + 6u
# => 4u가 안올바르면? ans = ( ans ) 뒤집은 4u
# 이러면 될 것 같은데?

#1. 개수 같은지 체크
#2. (, ) 서로 맞는지 체크
#3. u와 v로 분리시키기.
#4. u가 올바르면 u+v하기.
#5. u가 올바르지 않다면?
#6. ( v최종본 ) 뒤집은 u


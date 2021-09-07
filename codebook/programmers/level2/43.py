def check1(string): # 균형 체크
    cur = string[0]
    cnt = 1
    for i in range(1, len(string)):
        if cur == string[i] : cnt += 1 
        elif cur != string[i] : cnt -= 1
        if cnt == 0 : return [string[0:i+1], string[i+1:]]
            
def check2(string):
    if string[0] == ')' : return False
    stack = ['(']
    for st in string[1:]:
        if st == '(' : stack.append('(')
        if st == ')' : 
            if len(stack) == 0 : return False
            stack.pop()
    if len(stack) == 0: return True

    
def solution(p):
    answer = ''
    u_list = []
    string = p

    while True:
        u, v = check1(string)  
        u_list.append(u)
        if len(v) == 0 : break
        string = v
        
    print(u_list)    
    for s_index in range(len(u_list)-1, -1, -1):
        string = u_list[s_index]
        print(check2(string))
        if check2(string) : answer = string + answer # 문제 없으면 앞에 붙이기.
        else : 
            if len(string) == 2: 
                answer = '()' + answer
                continue
                
            string = string[1:len(string)-1]
            string_list = [string[i] for i in range(len(string))]
                    
            for i in range(len(string_list)): 
                if string_list[i] == ')' : string_list[i] = '('
                else : string_list[i] = ')'
            print(1,''.join(string_list) )
            answer = '(' + answer + ')' + ''.join(string_list) 

        print(string, answer)
    return answer

p = '()))((()'
print(solution(p))

# 뒤에서 부터 접근하자.
# u_list가 존재
# u1 u2 u3 u4 u5 v가 있다고 치자
# ..... u5가 븅신임 => ( v ) + 바꾼 u5 => answer
# u4가 븅신임 => ( answer ) + 바꾼 u4
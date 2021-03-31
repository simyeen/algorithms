N, M = map(int, input().split())

str_list = list(input().split())
str_list.sort()
check = [False for i in range(M+10)]
ans = []

def password(cnt):

    if cnt == N :
        check_str = [0, 0]
        for char in ans :
            if (check_str[0] >= 1 and check_str[1] >= 2) : break 
            if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
                check_str[0] += 1
            else : check_str[1] += 1
        if(check_str[0] >=1 and check_str[1] >=2):
            for char in ans :
                print(char,end="")
            print(" ")
            return
        else: 
            return
    
    for i in range(M) :
        
        if(check[i]) : continue
        
        check[i] = True
        ans.append(str_list[i])
        password(cnt+1)
        
        ans.pop()
        for j in range(i+1, M):
            check[j] = False

        

password(0)
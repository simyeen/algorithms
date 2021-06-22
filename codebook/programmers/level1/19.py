

def solution(n):
    answer = ''
    
    n = str(n)
    arr = []
    for i in range(len(n)):
        arr.append((n[i]))  
    tmp = sorted(arr, reverse = True)
    answer = int("".join(tmp))
    
    return answer

print(solution(118372))
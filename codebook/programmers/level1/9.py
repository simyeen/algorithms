
a = [1,2,3,4]
b= [-3,-1,0,2]
def solution(a, b):
    
    value = 0

    for i in range(len(a)):
        value += a[i]*b[i]

    answer = value
    return answer

print(solution(a,b))
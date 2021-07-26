from math import gcd    

def lcm(a,b): 
    return (a*b)//gcd(a,b)

def solution(arr):
    
    
    while True :
        if len(arr) == 1 : return arr[0]
        arr.append(lcm(arr.pop(), arr.pop()))
        
print(solution([2,6,8,15]))    
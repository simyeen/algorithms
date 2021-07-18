from itertools import permutations, product

def solution(A,B):
    
    total_list = [A,B]

    pro = list(product(*total_list))    
    print(pro)


solution([1,2,3],[4,5,6])
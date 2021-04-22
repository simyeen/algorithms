from itertools import combinations

distances = []
def get_distance(circle): pass
    

def solution():
    n = int(input())
    weak = list(map(int, input().split()))
    dist = list(map(int, input().split()))
    
    circle = []
    
    for i in range(len(weak)):
        circle.append(list(combinations(weak, i+1)))
    for i in range(len(circle), -1, -1):
        print(i)
        
    print(circle)

    return -1


solution()

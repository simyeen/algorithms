from itertools import combinations

distances = [[] for i in range(len(dist)+1)]
def get_distance(arr, i):

    

def solution():
    n = int(input())
    weak = list(map(int, input().split()))
    dist = list(map(int, input().split()))
    
    circle = []
    for i in range(len(weak)):
        circle.append(list(combinations(weak, i+1)))
    for i in range(len(circle)):
        get_distance(circle[i], i)

    print(circle)

    return -1


solution()

# 그리디로 접근해보자
# 근데 이때 원소를 기록할까 말까..??
# circle.pop()을 하면서 첫 번쨰 원소와 마지막 원소의 차이가 distance로 들어가게 하자. 이때 원소 개수도 같이 넣어주기.
# 만약 그리디로 빼면 바로 인덱스를 n-빼진 원소 수 부터 보는데 이중에서 가장 작은애로 들어가게 하자.
# 만약 안빠지면 max값을 기록해두다가 인덱스가 작은데도 max값이랑 작거나 크면 바로 continue하게 하자.
#  
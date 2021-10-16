def find_parent(parent, x):
    if parent[x] != x :
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    #a = find_parent(parent, a)
    #b = find_parent(parent, b)
    parent[b] = a


def get_parents(parent, x, arr):
    arr.append(x)
    if parent[x] != x :
        return get_parents(parent, parent[x], arr)
    return x

t = int(input())

for _ in range(t):
    ans = -1
    n = int(input())
    
    parent = [i for i in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    
    a, b = map(int, input().split())
    
    arr1, arr2 = [], []
    a_parent = get_parents(parent, a, arr1)
    b_parent = get_parents(parent, b, arr2)
    
    for p in arr1:
        if p in arr2 and arr2.index(p) != -1: 
            ans = p
            break
    print(ans)


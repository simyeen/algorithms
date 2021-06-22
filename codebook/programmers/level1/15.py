
def gcd(n, m):
    if m == 0 : return n
    else : return gcd(m, n%m)

def solution(n, m):
    g = gcd(n,m)
    return [g, n*m//g]

print(solution(18,6))

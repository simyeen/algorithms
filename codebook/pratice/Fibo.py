# 미리 배열 저장해서 반복문.
def f_1(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


# 재귀를 통해서
def f_2(n):
    if n< 2:
        return n
    else:
        return f_1(n-1) + f_1(n-2)


# 메모이제이션
dic = {1:1, 2:1}

def fib_memoization(n):
    print(dic)
    if n in dic:
        return dic[n]
    
    dic[n] = fib_memoization(n-1) + fib_memoization(n-2)
    return dic[n]

print(f_1(5))
print(f_2(5))
print(fib_memoization(20))


def fact(N):
    if N == 2:
        return 1

    return N * fact(N-1)


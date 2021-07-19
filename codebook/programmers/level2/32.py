NOTATION = '0123456789ABCDEF'

def num_sys(number,base): # 진법 변환
    q, r = divmod(number,base)
    n = NOTATION[r]
    return num_sys(q, base) + n if q else n

def trans(base,t,m,p):
    strings = ''
    for i in range(m*t + (p+1)):
        strings += str(num_sys(i,base))
    return list(strings)

def solution(n, t, m, p):
    answer = []
    data = trans(n,t,m,p)

    for i in range(t):
        index = m*i + (p-1)
        answer.append(data[index])
    ans = "".join(answer)

    return ans

print(solution(16,16,2,2))
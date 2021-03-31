E, S, M = map(int, input().split())

n = 1
e, s, m = 1, 1, 1
while True:
    if e == E and s == S and m == M:
        print(n)
        break

    e += 1
    s += 1
    m += 1
    n += 1

    if e > 15:
        e -= 15
    if s > 28:
        s -= 28
    if m > 19:
        m -= 19

E, S, M = map(int, input().split())

E_ = 0
S_ = 0
M_ = 0

result = 0

# 계속 더하고 이상 넘어가면 1로 바꿔주고...
while not (E == E_ and S == S_ and M == M_):
    E_ += 1
    if E_ == 16:
        E_ = 1
    S_ += 1
    if S_ == 29:
        S_ = 1
    M_ += 1
    if M_ == 20:
        M_ = 1

    result += 1

print(result)
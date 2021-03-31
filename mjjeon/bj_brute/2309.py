import sys

D = [0 for _ in range(9)]
H = [0] * 9
current_d1 = -1
current_d2 = -1

for i in range(9):
    H[i] = int(sys.stdin.readline())

for i in range(9):
    D[i] = sum(H[:i]) + sum(H[i+1:])

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if D[i] - H[j] == 100:
            current_d1 = i
            current_d2 = j
            break
    if current_d1 == i:
        break

current_d1 = H[current_d1]
current_d2 = H[current_d2]

H.remove(current_d1)
H.remove(current_d2)

H.sort()

for i in H:
    print(i)


# if i+j==sum(l)-100:l.remove(i);l.remove(j) 좋은 방법인듯...
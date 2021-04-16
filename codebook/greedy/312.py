from collections import deque

arr = deque(list(input()))

total = int(arr.popleft())

while arr :
    now = int(arr.popleft())
    if total == 0 or total == 1 or now == 0 or now == 1:
        total += now
    else :
        total *= now

print(total)

    
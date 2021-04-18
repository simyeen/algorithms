data = input()

alpha = []
number = 0
for item in data:
    target = ord(item)
    if 65 <= target <= 122:
        alpha.append(target)
    else:
        number += int(item)

alpha.sort()

for i in range(len(alpha)):
    alpha[i] = chr(alpha[i])
alpha.append(str(number))

print(''.join(alpha))

N = int(input())
result = 0
i = 1
j = 1
while j < len(str(N)):
    result += i * 9 * j
    i *= 10
    j += 1

result += (N - i + 1)* j

print(result)

# https://pacific-ocean.tistory.com/166
# 만약 n자리수의 숫자를 입력받았다면, n - 1자리수까지의 총 자리수를 더하고, n자리수의 숫자들은 따로 계산한다.
# 120을 입력받았다면, 두자리수까지의 총 합은 189(9 * 1 + 90 * 2)이다.
# 세자리수는 120 - 100 + 1을 해주고 자리수(3)을 곱해준다.

# 시간초과
# N = int(input())
# result = ''
# for i in range(1, N+1):
#     result += str(i)

# print(len(result))
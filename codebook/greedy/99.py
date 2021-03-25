# # 1이 될 때까지
# n, k = map(int, input().split())

# cnt = 0

# while(n != 0):
#     if(n == 1):
#         break
#     elif n % k == 0:
#         cnt += 1
#         n /= k
#         continue
#     n -= 1
#     cnt += 1

# print(cnt)

# 내 풀이 : 최선의 해 => 나누기 부터 실행 후 continue를 통해서 계속 나눈다.
# 즉) 최대한 나눌 수 있는 만큼 나누는 그리디 방법이다.

n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    result += n-target
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += n-1
print(result)

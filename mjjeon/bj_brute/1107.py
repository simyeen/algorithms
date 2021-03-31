import sys
input = sys.stdin.readline
def check(num):
    num = list(str(num))
    for i in num:
        if i in s: return False
    return True
n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n - 100)
for i in range(1000001):
    if check(i): result = min(result, len(str(i)) + abs(i - n))
print(result)

# https://pacific-ocean.tistory.com/424

# 반례:  https://www.acmicpc.net/board/view/46120

# 틀렸습니다 방식 똑같이 했습니다. 또옥가은데 
# import sys

# N = sys.stdin.readline().rstrip()
# M = int(sys.stdin.readline())
# if M == 0:
#     M_list = []
# else:
#     M_list = list(map(int, sys.stdin.readline().split()))

# cnt = abs(100 - int(N))

# for i in range(1000001): #  500001 틀렸ㅅㅂ니다 
#     is_not_in = True
#     for num in N:
#         if num in M_list:
#             is_not_in = False
#             # break
#     if is_not_in:
#         cnt = min(cnt, len(str(i)) + abs(i - int(N)))

# print(cnt)

# 버리고 숫자 0부터 10000000까지... 하겠습니다..
# N = sys.stdin.readline().rstrip()
# M = int(sys.stdin.readline())
# if M == 0:
#     M_list = []
# else:
#     M_list = list(map(int, sys.stdin.readline().split()))

# cnt = 0
# number = ''

# if int(N) == 100:
#     print(0)
# else:

#     after_for = True
#     for i in N:
#         button_num = int(i)

#         # 틀렸습니다 -> 숫자 개수에 따라서 계속 하는 게 문제..
#         # 반례
#         # 100000
#         # 9
#         # 0 1 2 3 4 5 6 7 8
#         if button_num in M_list:
#             min_diff = 10
#             min_val = -1
#             for i in range(10):
#                 if min_diff > abs(i - button_num) and i not in M_list:
#                     min_diff = abs(i - button_num)
#                     min_val = i
#             if min_val != -1:
#                 button_num = min_val
#             else:
#                 after_for = False
#                 # 반례 
#                 # 1
#                 # 10
#                 # 0 1 2 3 4 5 6 7 8 9  
#                 # 99

#         # 틀렸습니다
#         # if button_num in M_list:
#         #     min_diff = 10
#         #     min_val = -1
#         #     for i in range(9):
#         #         if min_diff > abs(i - button_num) and i not in M_list:
#         #             min_diff = abs(i - button_num)
#         #             min_val = i
#         #     if min_val != -1:
#         #         button_num = min_val


#         # 문제 테스트 3번 안됨..
#         # while button_num in M_list:
#         #     button_num -= 1
#         #     if button_num == -1:
#         #         button_num = 9

#         number = number + str(button_num)
#         cnt += 1

#     if after_for:
#         cnt += abs(int(N) - int(number)) # +, - 버튼...
#     else:
#         cnt = 10000000

#     print(min(abs(int(N) - 100), cnt))
#     # 틀렸습니다
#     # print(min(abs(int(N) - 100), cnt))
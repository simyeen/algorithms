# 1. nxn행렬 생성
# 2. change 함수와 check 함수 만들기
# 3. 얼마만큼의 원소를 change할 건지 고민한다.
# 4. change할 때 마다 계속 check 해주기
# 5. check결과 max값을 static 혹은 전역변수로 계속 기억해두기


# n = int(input())
# max_value = 1


# def swap(a, b):
#     temp = a
#     a = b
#     b = temp


# def check_row(row):
#     global max_value
#     cnt = 1
#     for j in range(n-1):
#         # print("check_row in row, col, cnt[idx] = ", row, j, cnt[idx])
#         if candy[row][j] == candy[row][j+1]:
#             cnt += 1
#         else:
#             cnt = 1
#         if max_value < cnt:
#             max_value = cnt


# def check_col(col):
#     global max_value
#     cnt = 1
#     for i in range(n-1):
#         if candy[i][col] == candy[i+1][col]:
#             cnt += 1
#         else:
#             cnt = 1
#         if max_value < cnt:
#             max_value = cnt


# candy = []
# for i in range(n):  # 초기화 해주기.
#     candy.append(list(input()))

# for i in range(n-1):  # 행
#     for j in range(n-1):  # 열
#         swap(candy[i][j], candy[i][j+1])  # 오른쪽과 바꾸기.
#         check_row(i)
#         check_col(j)
#         check_col(j+1)
#         swap(candy[i][j], candy[i][j+1])  # 원래대로 돌리기.
#         swap(candy[i][j], candy[i+1][j])  # 아래쪽과 바꾸기.
#         check_row(i)
#         check_row(i+1)
#         check_col(j)
#         swap(candy[i][j], candy[i+1][j])  # 원래대로 돌리기.
#         print(i, j)

# for j in range(n-1):  # 제일 마지막 행
#     swap(candy[n-1][j], candy[n-1][j+1])
#     check_row(n-1)
#     check_col(j)
#     check_col(j+1)
#     swap(candy[n-1][j], candy[n-1][j+1])  # 원래대로 돌리기.

# for i in range(n-1):  # 제일 마지막 열
#     swap(candy[i][n-1], candy[i+1][n-1])
#     check_row(i)
#     check_row(i+1)
#     check_col(n-1)
#     swap(candy[i][n-1], candy[i+1][n-1])  # 원래대로 돌리기.

# print(max_value)

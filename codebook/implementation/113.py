# n = int(input())


# cnt = 0

# for hours in range(n+1) : 
#     if '3' in str(hours):
#         cnt+=1
#     for minute in range(60) :
#         if '3' in str(minute) :       
#             cnt+=1
#         for second in range(60) :
#             if '3' in str(second) :
#                 print(second, cnt)
#                 cnt+=1

# print(cnt)


n = int(input())
cnt = 0

for hours in range(n+1) : 
    for minute in range(60) :
        for second in range(60) :
            if '3' in str(hours) + str(minute) + str(second) :
                cnt+=1

print(cnt)



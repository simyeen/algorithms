n = input()
leng = len(n)

cnt = 1
n = int(n)

if leng == 1:
    print(n * 1)
    exit()
elif leng == 2:
    print((n-9)*2 + 9 * 1)
    exit()
elif leng == 3:
    print((n-99)*3 + 90*2 + 9)
    exit()
elif leng == 4:
    print((n - 999)*4 + 900*3 + 90*2 + 9)
elif leng == 5:
    print((n-9999)*5 + 9000*4 + 900*3 + 90*2 + 9)
elif leng == 6:
    print((n-99999)*6 + 90000*5 + 9000*4 + 900*3 + 90*2 + 9)
elif leng == 7:
    print((n-999999)*7 + 900000*6 + 90000*5 + 9000*4 + 900*3 + 90*2 + 9)
elif leng == 8:
    print((n-9999999)*8 + 9000000*7 + 900000 *
          6 + 90000*5 + 9000*4 + 900*3 + 90*2 + 9)
elif leng == 9:
    print((n-99999999)*9 + 90000000*8 + 9000000*7 +
          900000*6 + 90000*5 + 9000*4 + 900*3 + 90*2 + 9)

# minus = 0
# for i in range(leng-2, -1, -1):
#     minus += 9 * (10**i)

# for i in range(leng-2, -1, -1):
#     cnt += i*9*(10**i)
#     print(i)
#     print(i*9*(10**i))

# print(leng*(n-minus) + cnt)

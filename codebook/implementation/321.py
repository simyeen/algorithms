data = input()

half = len(data)//2

count1 = 0
count2 = 0

for i in range(half) :
    num = int(data[i])
    count1 += num
for i in range(half,len(data)):
    num = int(data[i])
    count2 += num

if count1 == count2:
    print('LUCKY')
else:
    print('READY')
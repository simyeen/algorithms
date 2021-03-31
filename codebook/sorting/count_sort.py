arr = [7,5,0,0,3,1,6,2,0,1,4,6,0,2]

count = [0]*(max(arr)+1)

for i in range(len(arr)):
	count[arr[i]] += 1 # 각 데이터에 해당되는 인덱스의 값을 증가시킨다.

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end = ' ')
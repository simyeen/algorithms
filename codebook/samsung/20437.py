n = int(input())


cmds = []
for _ in range(n):
    w = input()
    k = int(input())
    cmds.append((w, k))

for cmd in cmds:
    w, k = cmd[0], cmd[1]
    dict = {}

    for i in range(len(w)):
        key = w[i]
        if key not in dict :
            dict[key] = [1,[i]]
        else : 
            dict[key][0] += 1
            dict[key][1].append(i)

    mylist = []
    for key in dict:
        count = dict[key][0]
        if count >= k : mylist.append(dict[key][1])

    if len(mylist) == 0 : 
        print(-1)
        continue
    
    
    min_value, max_value = 1e9, -1e9

    for arr in mylist:
        for i in range(len(arr) - k + 1):
            leng = arr[i + k - 1] - arr[i] + 1
            min_value = min(min_value, leng)
            max_value = max(max_value, leng)
    print(min_value, max_value)

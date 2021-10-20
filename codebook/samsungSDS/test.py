def sorted_data(arr):
    new_data = [[0 for _ in range(m)] for _ in range(n)]

    tmp_data = []
    for j in range(m):
        tmp = ''
        for i in range(n):
            if arr[i][j] != 0:
                tmp += str(arr[i][j])
        tmp = tmp.zfill(n)
        tmp_data.append(list(tmp))

    print(tmp_data)
    for i in range(m):
        for j in range(n):
            print(i,j)
            new_data[j][i] = int(tmp_data[i][j])

    return new_data


n, m = 4,3
arr = [
    [0,1,0],
    [0,0,0],
    [1,0,0],
    [0,0,0]
]

print(sorted_data(arr))
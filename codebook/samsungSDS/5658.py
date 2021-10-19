
dict = {
    'A' : 10, 'B' : 11, 'C' : 12,
    'D' : 13, 'E' : 14, 'F' : 15
}

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    string = input()
    leng = n//4

    st_set = set()
    st_list = list(string)
    for _ in range(leng):
        for i in range(0, n, leng):
            st = st_list[i:i+leng]
            st_set.add(''.join(st))
        st_list.insert(0, st_list.pop()) # 시계 방향 회전.

    ans_list = list(st_set)
    ans = []
    for st in ans_list:
        num = 0
        for i in range(len(st)):
            if st[i] in dict:
                num += dict[st[i]] * (16** (len(st)-i-1))
            else: num += int(st[i]) * (16** (len(st)-i-1))
        ans.append(num)
    ans.sort(reverse=True)
    print(ans[k-1])





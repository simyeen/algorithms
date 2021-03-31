n = int(input())
arr = set(map(int, input().split()))
# set(집합) type을 사용하면 오르차순 + 중복제거로 되기때문에 추가적인 sorting이 필요없다.
m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i in arr :
        print('yes')
    else:
        print('no')
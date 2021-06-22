def no_continuous(s):
    a = []
    for i in s:
        print(i)
        print(a[-1:], [i])
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "112233445566" ))
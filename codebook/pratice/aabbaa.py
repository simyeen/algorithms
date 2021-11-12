def get_p(st):
    half = len(st)//2
    for i in range(half):
        if st[i] != st[len(st)-1-i]:
            return False
    return True

def get_p2(st):
    print(st)
    if len(st)<2:
        return True
    if st[0] != st[-1]:
        return False
    return get_p2(st[1:-1])




print(get_p('abnbna'))
print(get_p2('abnbna'))
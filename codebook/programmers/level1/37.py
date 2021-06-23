def solutions(a, s):
    answer = 0
    for a, s in zip(a,s):
        if s:
            answer += a
        else :
            answer -= a
    return answer

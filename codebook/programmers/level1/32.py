def solution(strings, n):
    answer = []

    strings.sort()
    strings.sort(key = lambda x :( x[n]))

    return strings

print(solution(["abce", "abcd", "cdx"]	, 1))
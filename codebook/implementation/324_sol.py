
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # step만큼 증가시키면서 이전 문자열과 비교하기.
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # compressed = counter >= 2 ? str(count) + prev : prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

s = input()
print(solution(s))

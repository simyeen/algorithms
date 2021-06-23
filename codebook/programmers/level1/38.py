def solution(participant, completion):
    
    data = dict()
    for name in participant:
        data[name] = 0
    for name in participant:
        data[name] += 1
    for name in completion:
        data[name] -= 1
    for name in participant:
        if data[name] == 1:
            return name

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))


participant	= ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    
    length = len(participant)
    participant.sort()
    completion.sort()
    
    count = [0] * length

    for char in participant:
        if char not in completion:
            return char



    return answer

print(solution(participant, completion))
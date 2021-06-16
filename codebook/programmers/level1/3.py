participant	= ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    
    length = len(participant)
    participant.sort()
    completion.sort()

    check = [False] * length

    for char in completion:
        for i in range(length):
            if check[i] == False :
                if participant[i] == char:
                    check[i] = True

    for i in range(len(check)):
        if check[i] == False:
            answer = participant[i]
    
    return answer

print(solution(participant, completion))
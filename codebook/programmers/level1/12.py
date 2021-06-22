

def solution(phone_number):
    answer = ''
    
    for _ in range(len(phone_number)-4): # answer += '*' * (len(p_num) -4)로 축약가능.
        answer += '*'
    answer += phone_number[len(phone_number)-4:]
    return answer

    

print(solution("1234"))
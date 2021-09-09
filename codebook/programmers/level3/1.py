# 추석 트래픽문제.
def check_time(check_time, target): 

    t_start,t_end = target
    if not (t_end < check_time or check_time+999 < t_start) : return True
    return False

    

def solution(lines):
    times = []
    for line in lines:
        line = line[11:]
        line = line.split()
        S, T = line[0], int(float(line[1][:len(line[1])-1])*1000)
        S = (int(S[:2])*3600 + int(S[3:5])*60 + int(S[6:8]))*1000 + int(S[9:])
        times.append((S-T+1,S))

    ans = []
    for time in times: # 한 구간의 처음과 끝에 대하여.
        start, end = time
        
        start_cnt, end_cnt = 0, 0
        for target in times : 
            if check_time(start,target) : start_cnt +=1 
            if check_time(end,target) : end_cnt += 1
        ans.append(max(start_cnt, end_cnt))
    
    return max(ans)

lines2 =  [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]

lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))


# 임의 시간부터 1초간 처리하는 요청의 최대 개수는?
# S, T  => 소숫점 3째자리까지 존재.
# ms단위로 각 시작 => 종료시간 까지 모두 기록가능.
# 문제는 어떻게 임의시간 단위로 끊어서 볼 수 있을까요???
# ms단위로 하면 억 단위라서 무조건 시간초과가 나옴.
# 일단 문제는 그리디로 하는게 맞는거 같습니다.
# 그렇다면 어떤식으로 그리디로 처리할거세요?
# 각 처음시간-1, 각 끝 시간-1 로만 검사하면 어떨까요?

# 1번째에의 시작 + 1ms 앞에서 => 1번째애의 끝 - 1ms에서!













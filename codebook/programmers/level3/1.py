import re

def solution(lines):
    answer = 0
    data = []
    for line in lines:
        line = line[11:]
        first = line.split()
        S, T = first[0], first[1][:len(first[1])-1]
        T, p = int(float(T)*1000), re.compile('\d+')
        S = p.findall(S)
        time = (int(S[0])*3600 + int(S[1])*60 + int(S[2]) )*1000 + int(S[3])
        data.append((time, T))
    
    time_list = []
    for i in range(len(data)):
        time = data[i]
        time_list.append((time[0]-time[1]+1, time[0]))
        
    start, end = time_list[0][0], time_list[-1][1]
    
    max_value = -1e9
    for i in range(start,end+1):
        cnt = 0
        for time in time_list:
            start, end = time
            if i <= start or end <= i+999 : cnt += 1
            print(cnt)
        max_value = max(cnt, max_value)
    
    
    return answer


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


# data => 각 트래픽의 시작과 끝 시각을 기록해놓음.
# start부터 end까지 1씩 증가시키자.
# 범위안에 
# start => end 까지 1단위로 보자...
# 











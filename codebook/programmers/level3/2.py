# 셔틀 버스
def solution(n, t, m, timetable):
    
    buses, arrive_list = [540 + t*(i) for i in range(n)], []
    timetable.sort()
    for time in timetable:
        time = time.split(':')
        time = int(time[0])*60 + int(time[1])
        arrive_list.append(time)
    print(buses)
    print(arrive_list)

    buses_count = [[] for _ in range(len(buses))]
    check_arrive = [False for _ in range(len(arrive_list))]

    for i in range(len(buses)):
        for j in range(len(arrive_list)):
            if check_arrive[j] == True : continue # 이미 탑승한 애            
            if len(buses_count[i]) < m and buses[i] >= arrive_list[j]: 
                buses_count[i].append(j)
                check_arrive[j] = True

    print(buses_count)
    if len(buses_count[-1]) < m : 
        tmp = divmod(buses[-1], 60)
    else : 
        tmp = divmod(arrive_list[buses_count[-1][-1]]-1,60)
    print(tmp)
    ans = str(tmp[0]).zfill(2) + ':' + str(tmp[1]).zfill(2)
    return ans

n,t,m,timetable = 2, 10, 2, ["09:10", "09:09", "08:00"]

tmp = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

print(solution(n,t,m,timetable))


# 1. n, t와 그거에 대한 수용인원 m에 대한 배열 생성하기.
# 2. 

# 셔틀버스 9시부터 출발 => n회 t분 간격
# 1. 버스종류 싹 알아내자.
# 2. 가장 마지막 버스에 타려고 노력하자.
# 3. 콘은 무조건 동시간 마지막에 탄다.
# 4. 버스에 누가 타는지 알아내기
# 5. => m 미만이다 => 그냥 탑승 가능 ok
# 6. m이상이다 => 제일 마지막에 존재하는 놈 보다 1분먼저 와야댄다.
# 7. 근데 만약 57 58 59면 58에 가능 ok
# 8. 근데 만약 59 59 59면 58에 가능 ok

import re

def solution(info, query):
    answer = []

    p = re.compile('\D+|\d+')

    arr = []
    for i in info:
        i = i.replace(' ','')
        #print(re.findall(p,i))
    
    for q in query:
        #q = q.replace(' ','')
        q = q.replace('and','')
        print(re.findall(p,q))

    a = 0b11111111
    print(a)
    b = 0b10000000
    print(a^b)

    return answer

i = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
q = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(i,q))

# 지원자  => 1 2 3 4 5 
# 개발언어, 직군, 경력, 소울푸드, 점수

# 쿼리 => 1 2 3 4 5
# 개발언어 직군 경력 소울푸드 점수

# info => 지원자 점수 공백하나로 전부다 나누기 가능
# query ' and' 라는 단어 전부 제거하고 공백으로 나누기

# 각 query에 대해서 만족하는 info 수를 구하는 문제다.
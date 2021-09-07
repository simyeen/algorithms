dict = {chr(i + 64): i for i in range(1, 27)}

def solution(msg):
    answer = []
    
    i = 0
    cnt = 27
    t = 10
    while i < len(msg):
        
        tmp = ''
        while t : # 사전에 없는 값을 찾을 때 까지    
            
            tmp += msg[i]
            print(i,msg[i], tmp)
            i += 1
            t -= 1
            if tmp not in dict or i == len(msg) : break
        
        cnt, i = cnt + 1, i - 1
        answer.append(dict[tmp[:len(tmp)-1]])
    
    
    return answer

msg = 'KAKAO'
print(solution(msg))

#KAKAO
#K => KA X 등록 27 K=11
#A => AK X 등록 28 A=1

#1. 한글자를 본다. 계속 늘린다. 사전에 존재하지 않는 string단위이면 등록한다.
#2. 등록하면서 바로 그 전 string의 인덱스를 answer에 담는다.
#3. 종료조건 => K A KA O 마지막 문자열이면 종료할 것
#4. K A K A KA O면? K => A => KA =>  KA 


























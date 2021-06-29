dic = {

 '1' : '1',     '6' : '14'
,'2' : '2',	    "7" : '21'
,'3' : '4',	    '8' : '22'
,'4' : '11',	'9': '24'
,'5' : "12",	'10':	'41'

}

def solution(n):
    answer = ''
    num = str(n)

    arr = []
    for i in range(len(n)):
        arr.append((n[i], len(n)-1-i))
    
    check = [0,3,5,6,7,8,9]

    
    while True:

        for i in num:
            if i in check: break
            else : return answer # 전부다 124로만 이루어진 경우
        
        for i in 



    return answer


print(solution('12345'))



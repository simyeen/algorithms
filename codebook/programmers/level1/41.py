# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #

left_nums = [1, 4, 7]
right_nums = [3, 6, 9]
mid_nums = [2, 5, 8, 0]
phones = { 
    1: (0,0), 2:(0,1), 3:(0,2),
    4: (1,0), 5: (1,1), 6:(1,2),
    7: (2,0), 8: (2,1), 9 :(2,2),
    -1: (3,0) , 0 : (3,1), -2 : (3,2)
    }

def choice(num, lcur, rcur, hand):

    target = phones[num]
    x, y = target[0], target[1]
    l_distance = abs(phones[lcur][0] - x) + abs(phones[lcur][1]-y) 
    r_distance = abs(phones[rcur][0] - x) + abs(phones[rcur][1]-y) 
    
    if l_distance == r_distance:
        if hand == 'right': return True
        else : return False
    elif l_distance > r_distance:
        return True
    else : return False
    
    
def solution(numbers, hand):
    
    answer = ''
    lcur = -1
    rcur = -2

    for num in numbers:
        if num in left_nums:
            lcur = num
            answer += 'L'
        elif num in right_nums:
            rcur = num
            answer += 'R'
        else : 
            if choice(num, lcur, rcur, hand) == True:
                rcur = num
                answer += 'R'
            else : 
                lcur = num
                answer += 'L'

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	
hand = "left"
print(solution(numbers,hand))
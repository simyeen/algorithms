days = ['FRI','SAT','SUN','MON','TUE','WED','THU',]

year = 366

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]
month29 = [2]

def solution(a, b):

    some = 0
    for i in range(1, a):
        if i in month31:
            some += 31
        elif i in month30:
            some += 30
        else : some += 29
    
    target = (some+b) % 7
    print(target)
    return days[((some+b) % 7) -1]


print(solution(5,24))
operators = ['+', '-', '*', '/', '']

def solution(N, number):
    if N == number : return 1
    d = [[] for _ in range(10)]
    d[1].append(str(N))
    
    for i in range(2,5):
        for acc in d[i-1]:
            string = acc
            for op in operators:
                if int(string) == 0 and op == '' : string = str(N)
                else : string += op + str(N)
                result = int(eval(string))
                d[i].append(str(result))
                string = acc
    for i in d : 
        print(i)
        print()
    return -1

print(solution(5,12))


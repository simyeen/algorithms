board = [   [0,0,0,0,0],
            [0,0,1,0,3],
            [0,2,5,0,1],
            [4,2,4,4,2],
            [3,5,1,3,1]
        ]
        
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    mylist = []

    for i in moves:
        target = i-1
        for item in board:
            if item[target] != 0:
                tmp = item[target]
                item[target] = 0
                if [tmp] == mylist[-1:]:
                    mylist.pop()
                    answer += 2
                else :
                    mylist.append(tmp)
                break

    return answer

print(solution(board, moves))
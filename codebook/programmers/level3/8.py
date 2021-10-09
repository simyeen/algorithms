# from collections import deque

# def bfs(begin, target, dict, check_dict):
#     q = deque()
#     q.append([begin,0])
#     check_dict[begin] = True
#     ans = []
#     while q:
#         word, cnt = q.popleft()
#         if word == target : return cnt
#         for key in dict[word]:
#             if check_dict[key] : continue
#             q.append([key,cnt+1])
#             check_dict[key] = True
    
#     return 0


from collections import deque

def bfs(begin, target, dict, check_dict):
    q = deque()
    q.append([begin, 0])
    check_dict[begin] = True
    while q:
        word, cnt = q.popleft()
        if word == target : return cnt
        for key in dict[word]:
            if check_dict[key] : continue
            q.append([key,cnt+1])
            check_dict[key] = True
    return 0

def solution(begin, target, words):
    if target not in words : return 0
    dict, check_dict = {}, {}
    words = [begin] + words
    for i in range(len(words)):
        dict[words[i]] = []
        check_dict[words[i]] = False
        for j in range(len(words)):
            if i == j : continue
            cnt = 0
            for k in range(len(begin)):
                if words[i][k] == words[j][k] : cnt+=1
            if cnt == len(begin)-1 : dict[words[i]].append(words[j])
    return bfs(begin, target, dict, check_dict)
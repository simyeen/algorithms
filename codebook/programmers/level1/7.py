import re

new_id = "=.="

def solution(new_id):
    answer = ''
    new_id = (new_id.lower())
    new_id = re.sub(r"[^a-z0-9._-]","",new_id)
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)

    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]

    return answer

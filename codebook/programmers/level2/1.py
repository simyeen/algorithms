import re

def solution(s):
    
    while True:
        if not s :
            return 1
        if s :
            before = len(s)
            s = re.sub('(([a-z])\\2{1,})','',s)
            after = len(s)
            if before == after :
                return 0
            
            
    
    
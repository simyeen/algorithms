import re

def solution(files):
    p = re.compile('[\D]+|[\d]+|[.*]')
    return sorted(files, key=lambda x : (p.findall(x)[0].lower(), int(p.findall(x)[1])))

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))
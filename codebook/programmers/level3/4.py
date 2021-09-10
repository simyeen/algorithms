# 매칭 점수
import re

def solution(word, pages):
    answer = 0
    
    p = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.MULTILINE)  

    links = []  
    for page in pages: 
        page = page.replace('\n','')
        tmp = []
        link = p.findall(page)
        for li in link:
            if 'html' not in li: tmp.append(li)
        links.append(tmp)
    print(links)

    word = [word.upper(), word.lower()]
    
    p = re.compile('<body>.*<body>', re.I|re.S)
    print(p)
    for page in pages: 
        word_tmp = p.findall(page)
        print(word_tmp)


    return answer

word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

print(solution(word,pages))

# 1. meta태그 => content얻어내기.
# 2. a태그로 => 외부링크 알아내기.


# 목표 : 검색어에 대한 매칭점수를 구하자.
# 기본점수, 외부링크수, 링크점수, 매칭점수 존재.
# 기본점수 => 텍스트 중 검색어가 등장하는 횟수
# => 기본점수는 전부다 대문자로 보자.
# 아웃링크랑
# 자기한테 들어오는 인링크 => 기본점수/외부링크수의 총합 
# 매칭점수 = 기본점수(검색어로 구하기) + 링크점수(자기한테 들어온애 보고 구하면 됨.)


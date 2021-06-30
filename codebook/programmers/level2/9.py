def solution(phone_book):
    answer = True
    
    book = sorted(phone_book, key = lambda x : len(x))
    for i in book:
        leng = len(i)    
        for j in book:
            
            if i == j[:leng] : return False
    
    return True
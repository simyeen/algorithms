def solution(phone_book):
    answer = True
    
    book = sorted(phone_book, key = lambda x : len(x))
    for i in range(len(book)):
        leng = len(book[i])    
        for j in range(i+1, len(book)):
            if book[i] == book[j][:leng] : return False
    return True

phone_book = ["123","456","789"]
print(solution(phone_book))


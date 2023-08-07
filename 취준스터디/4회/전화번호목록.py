def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x))
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                if phone_book[j].index(phone_book[i]) == 0:
                    return False
    return True
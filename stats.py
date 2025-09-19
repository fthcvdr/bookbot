def words_count(book_text: str):
    return len(book_text.split())

def character_counter(book_texts: str):
    lower_book = book_texts.lower()
    char_dic = {}
    for char in lower_book:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] += 1
    return char_dic

def short_on(items):
    return items["num"]

def key_value(book_dic: dict):
    new_list = []
    for key in book_dic:
        new_dic ={}
        new_dic["char"] = key
        new_dic["num"] = book_dic[key]
        new_list.append(new_dic)
    new_list.sort(reverse=True, key=short_on)
    return new_list

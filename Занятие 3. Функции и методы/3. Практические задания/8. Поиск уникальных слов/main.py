# TODO реализовать функцию
def get_unique_words(word):
    list_word = word.split()
    list_word = set(list_word)
    list_word = list(list_word)
    list_word.sort()
    return list_word

print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))

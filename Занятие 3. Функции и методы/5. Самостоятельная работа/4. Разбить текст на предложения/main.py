# TODO реализовать функцию
def get_sentences_list(text):
    list = text.split('.')
    new_list = []
    for str in list:
        if str != '':
            new_list.append(str.strip())
    # print(new_list)
    return new_list


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))

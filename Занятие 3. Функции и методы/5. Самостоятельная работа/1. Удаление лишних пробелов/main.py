# TODO реализовать функцию
def remove_whitespace(str):
    new_str = ''
    for i, char in  enumerate(str):
        # print (i, char)

        if(char == ' '):
            if( i > 0 and str[i-1] != ' '):
                new_str += char
        else:
            new_str += char



        # print(new_str)

    return new_str


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))

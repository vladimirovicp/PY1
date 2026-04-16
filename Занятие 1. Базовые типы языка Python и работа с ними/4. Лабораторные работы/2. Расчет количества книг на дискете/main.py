# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.4 * 1024 *1024
book_page = 100
book_line = 50
book_symbol = 25
book_symbol_weight = 4

book = book_page * book_line * book_symbol * book_symbol_weight

print("Количество книг, помещающихся на дискету:", round(disk / book))

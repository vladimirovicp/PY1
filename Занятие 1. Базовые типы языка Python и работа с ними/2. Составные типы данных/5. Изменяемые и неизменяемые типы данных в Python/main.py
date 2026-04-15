# TODO исправьте опечатку в слове
fruits = ["яблоко", "банан", "опельсин", "виноград"]
word = fruits[2]
fix_word = "а" + word[1:]
fruits[2] = fix_word
print(fruits)
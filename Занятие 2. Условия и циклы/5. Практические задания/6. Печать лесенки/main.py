# TODO С помощью цикла for распечатайте лесенку
number = 4
rez = ''
for value in range(1, number + 1):
    for numberSimvol in range(value):
        rez += '*'
    print(rez)
    rez=''

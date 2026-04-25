import os.path

INPUT_FILE = "input.txt"


OUTPUT_FILE = "output.txt"


def task():
    # TODO построчно записать лесенку в файл

    with open(OUTPUT_FILE, "w") as f:
        for i in range(1,11):
            data = '*' * i
            f.write( data + '\n')

if __name__ == '__main__':
    # Необходимо для проверки
    task()
    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for line in file:
            print(line, end="")

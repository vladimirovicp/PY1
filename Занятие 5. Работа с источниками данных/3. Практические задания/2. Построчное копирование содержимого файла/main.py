INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    # TODO перезаписать содержимое одного файла в другой

    with open(INPUT_FILE, "r", encoding="utf-8") as f_i:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f_o:
            for line in f_i:
                new_line = line.upper()
                f_o.write(new_line)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for current_line in file:
            print(current_line, end="")

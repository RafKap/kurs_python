def get_content():
    file_to_open = input("Put file name -> ")
    file_to_open = file_to_open + ".txt"
    with open(file_to_open, encoding="UTF-8") as fopen:
        content = fopen.readlines()
    return content


def main():
    quotes = get_content()
    for _ in quotes[0:5]:
        print(_.strip())
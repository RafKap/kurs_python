import random

with open('FILES_01.txt', encoding="UTF-8") as fopen:
    content_list = fopen.readlines()
    line_today = random.choice(content_list)
    print(line_today)

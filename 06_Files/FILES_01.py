import random

file_to_open = input("Put file name -> ")
file_to_open = file_to_open + ".txt"
with open(file_to_open, encoding="UTF-8") as fopen:
    content_list = fopen.readlines()
    line_today = random.choice(content_list)
    width = 50

    quote = line_today.split(" - ")
    quote_today = quote[0]
    autor = quote[1]
    print("Quote of the day is: \n")
    print("*" * width)
    print(quote_today.strip().center(width))
    print(autor.strip().center(width))
    print("*" * width)

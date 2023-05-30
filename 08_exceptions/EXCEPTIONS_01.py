
def main():
    x = [13, "string", 2.45, 0, True, False, (1, 2)]

    for i in x:
        try:
            a = i / 10
            print(a)
        except TypeError as te:
            print(te)


if __name__ == "__main__":
    main()
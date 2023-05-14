"""
Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
Co wiemy o tych numerach tych kart?
    All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
    MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
    American Express card numbers start with 34 or 37 and have 15 digits.

"""
def get_card_number():
    while True:
        card_nr = input("Insert card number here ->").replace(" ", "").replace("-", "")

        if is_card_number(card_nr):
            print("Yes, can be card number")
            break
        else:
            print("Nope! This is not card number")
            print("-- Try again! --")

    return card_nr


def is_card_number(num):
    if num.isdigit():
        return True
    else:
        return False


def is_visa(card_num):
    return str(card_num).startswith('4') and len(card_num) in (13, 16)


def is_mastercard(card_num):
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)
    return len(card_num) == 16 and start_condition


def is_amex(card_num):
    return len(card_num) == 15 and (card_num.startswith('34') or card_num.startswith('35'))

def main():
    number = get_card_number()
    print('💳 :', number)

    if is_visa(number):
        print(f'This card# {number} is Visa')
    elif is_mastercard(number):
        print(f'This card# {number} is MasterCard')
    elif is_amex(number):
        print(f'This card# {number} is Amex')
    else:
        print(f'This card# {number} is noone from above')


main()




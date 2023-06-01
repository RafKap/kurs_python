def check_mail(user_mail, base_mail):
    return True if user_mail in base_mail else False


base_mail = ['jan@gmail.com', 'anna@gmail.com', 'kamil@gmail.com']
input_mail = input('podaj adres mailowy: ')

if check_mail(input_mail, base_mail):
    print("Podany adres e-mail znajduje się w bazie maili.")
else:
    print("Podany adres e-mail nie znajduje się w bazie maili.")


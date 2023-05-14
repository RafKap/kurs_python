import random

WINNERS = {
    'rock': ("scissors", 'lizard'),
    'scissors': ('paper', 'lizard'),
    'paper': ('rock', 'spock'),
    'lizard': ('paper', 'spock'),
    'spock': ('scissors', 'rock')
}


possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]

def get_comp_choice():
    return random.choice(possible_actions)


def get_user_choice():

    while True:
        user_choice = input("Pick: paper, scissors, rock, lizard or spock: ")

        if user_choice in possible_actions:
            return user_choice
        else:
            print("Wrong value", "\n Try again!")


def show_result(comp, user):
    if comp == user:
        print(f'It is draw! Computer used -> {comp}, You use {user} ')
    elif comp in WINNERS[user]:
        print(f'You Won! Computer used -> {comp}, You use {user} ')
    else:
        print(f'YHou Lose! Computer used -> {comp}, You use {user} ')


def main():
    while True:
        comp = get_comp_choice()
        user = get_user_choice()

        # print(f'Computer used -> {comp}, You use {user}')
        show_result(comp, user)

        play_again = input("Wanna play again? Y/N ->")

        if play_again.upper() == "N":
            break

    print("Thanks for game!")

main()
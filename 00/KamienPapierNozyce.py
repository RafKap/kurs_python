import random

user_action = input("Enter a choice (rock, paper, scissors) :")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
#computer_action="rock"

#print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action not in possible_actions:
    print(user_action, "is not in list", "\n", "End of game")
    exit()

if user_action == computer_action:
    print("It is draw, because computer pick", computer_action, "and it is same as Your pick", user_action, "\n")
elif user_action == "scissors" and computer_action == "rock" or\
            user_action == "paper" and computer_action == "scissors" or\
            user_action == "rock" and computer_action == "paper":
        print("You lose, because computer pick", computer_action, "and You pick", user_action, "\n")
else:
    print("You win, because computer pick", computer_action, "and You pick", user_action, "\n")


print("End of game")

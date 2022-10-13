from data import data
from art import logo, vs
from replit import clear
import random


def account(random):
    name = random['name']
    description = random['description']
    country = random['country']
    return f"{name}, a {description}, {country}"


def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


# choose a random dictionary from data
def game():
    print(logo)
    score = 0
    should_continue = True
    random_account2 = random.choice(data)
    while should_continue:
        random_account1 = random_account2
        random_account2 = random.choice(data)
        while random_account1 == random_account2:
            random_account2 = random.choice(data)
        print(f"Compare A: {account(random_account1)}")
        print(vs)
        print(f"Against B: {account(random_account2)}")
        # Ask the user
        guess = input("Who has more Followers? Type 'A' or 'B' :-  ").lower()

        #check who has more followers
        follower_a = random_account1['follower_count']
        follower_b = random_account2['follower_count']
        # check if user chose right
        is_right = check_answer(guess, follower_a, follower_b)
        # if user is right
        # print the score and let them play more
        clear()
        print(logo)
        if is_right:
            score += 1
            print(f"You got it right! \ncurrent score: {score}")
        # if user is wrong
        # game over
        # Print the score
        else:
            should_continue = False
            print(f"You are wrong!!! \nfinal score: {score}")
            #ask if they wanna play again if yes then clear the current game and start a new game
            again = input("Do you wanna play again? Type 'y' or 'n' ").lower()
            if again == 'y':
                clear()
                game()
            else:
                print("have a great time!!")


game()

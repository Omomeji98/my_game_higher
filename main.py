import random
from data import data
from logo import logo,vs




def formatted_account(account):
    '''This function returns a data in a formatted form'''
    account_name = account["name"]
    account_descript = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descript} from {account_country}"


def check(user_guess, a_followers_account, b_followers_account):
    '''This functions compare the user guess with the original data and returns the account that has
    more followers'''
    if a_followers_account > b_followers_account:
        return guess == "a"
    else:
        return guess == "b"


# display art
print("Welcome to the Higher and Lower Game")
score = 0
print(logo)
# generate a random account from the game data
account_b = random.choice(data)
should_game_continue = True
while should_game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    # print(account_a)
    # print(account_b)
    # format the account data into printable format
    print("compare A: " + formatted_account(account_a))
    print(vs)
    print("Against B: " + formatted_account(account_b))


    # # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # check if user is correct

    # - get follower count of each account
    a_followers_account = account_a["follower_count"]
    b_followers_account = account_b["follower_count"]
    # - use if statement to check if user is correct
    is_correct = check(guess, a_followers_account,b_followers_account)
    if is_correct:
        score += 1
        print(f"You got it right. Your Score: {score}")
    else:
        should_game_continue = False
        print(f"You got it wrong. Your final score: {score}")
#  Give user feedback on their guess
# score keeping
# make the game repeatable
# making account at position B become the next account at position A.

from art import logo
import random
from game_data import data
from art import vs

def format_data(account):
     account_name=account['name']
     account_descr=account['description']
     account_country=account['country']
     return f'{account_name}, a {account_descr}, from {account_country}'

#Display art
print(logo)
#Generate a random account from the game data
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)
    
#print raedable data

print(f'Compare A: {format_data(account_a)}.')
print(vs)
print(f"Against B:{format_data(account_b)}.")


# ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower

# check if users is correct 
# get follower count of each account 
# use if statement to check if user is correct 

# give user feedback on their guess

#score keeping 
#make the game repeatable 
#Making account at position B become the next account at position A.
# clear the screeb between rounds.
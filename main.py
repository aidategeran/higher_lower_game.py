from art import logo
import random
from game_data import data

#Display art
print(logo)
#Generate a random account from the game data
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)
    
#print raedable data
print(account_a)
print(account_b)

# ask user for a guess

# check if users is correct 
# get follower count of each account 
# use if statement to check if user is correct 

# give user feedback on their guess

#score keeping 
#make the game repeatable 
#Making account at position B become the next account at position A.
# clear the screeb between rounds.
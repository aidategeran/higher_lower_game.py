from game_data import data
from art import logo

import random 

print(logo)

account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)


print(account_a)
print(account_b)


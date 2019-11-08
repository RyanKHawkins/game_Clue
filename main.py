# Title:  Clue
# Author:  Ryan Hawkins
# Update:  2019-10-20

import random

people = ["Col. Mustard"]
weapons = ["lead pipe", "rope"]
rooms = ["ballroom", "kitchen"]


# Create the murderer, murder weapon, and where the murder happened.
def setup_secret():
    secret = {}
    secret["murderer"] = random.choice(people)
    secret["weapon"] = random.choice(weapons)
    secret["scene"] = random.choice(rooms)
    return secret

print(setup_secret())
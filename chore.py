import random
from constants.constants import *

given_chores = []

def get_name():
    while True:
        name = input("What is your name: ")
        if name in KIDS:
            return name.lower()
        else:
            print("Uhm, I don't think thats your name...")
            continue

def get_random_chore(kid):
    new_chore = False
    l_score = 0
    o_score = 0
    e_score = 0
    
    while not new_chore:
        if kid == "olivia" and o_score < 8:
            o_score += 1
            chore = OLIVIA_CHORES[random.randint(0, len(OLIVIA_CHORES) - 1)]
        elif kid == "levi" and l_score < 8:
            l_score += 1
            chore = LEVI_CHORES[random.randint(0, len(LEVI_CHORES) - 1)]
        elif kid == "ezra" and e_score < 6:
            e_score += 1
            chore = EZRA_CHORES[random.randint(0, len(EZRA_CHORES) - 1)]
        else:
            return "You have no more chores! Good Job!"
        
        if chore not in given_chores:
            return chore

while len(given_chores) < len(ALL_CHORES):
    kid = get_name()
    if kid == "winnie":
        print("No Chores for you!")
    elif kid == "ezra":
        e_chore = get_random_chore(kid)
        if e_chore != "You have no more chores! Good Job!":
            given_chores.append(e_chore)
        print(e_chore)
    elif kid == "levi":
        l_chore = get_random_chore(kid)
        if l_chore != "You have no more chores! Good Job!":
            given_chores.append(l_chore)
        print(l_chore)
    else:
        o_chore = get_random_chore(kid)
        if o_chore != "You have no more chores! Good Job!":
            given_chores.append(o_chore)
        print(o_chore)

"""
Assumptions for earliest simulation playtesting purposes:
- all Mortys are max level (100) and fully trained (have max Effort Values)
- disobeying isn't a thing (Ricks/trainers are max level (50))
- if we can't randomize IV's (Inherent Values,) set to max (16) but rn we can(?)
- buffs/debuffs assumed to be 0 for now (implementation tbd)
- no perfect sim goes w/o poison and paralyze either, but this is no perfect sim (yet)
"""

import Fortuna

from app.base_mortys import *
# from app.attacks import *
from funktions import RandomTeams, roll_teams


def take_input():
    choice = input("What will you do? [a: Attack, s: Switch, r: Run]")

    if choice == "a":
        print("You chose Attack! Pick an Attack:")
        return pick_attack()
    elif choice == "s":
        print("You chose Switch! But you only have one Morty right now!")
        return take_input()
    elif choice == "r":
        print("You chose run. Are you sure?")
        return make_sure()
    else:
        print("Try again. [a: Attack, s: Switch, r: Run]")
        return take_input()


def pick_attack():
    gotron_attacks = ["Kick", "Protect", "Stare Down", "Combustion"]
    choice2 = input(f"Which Attack? [1: {gotron_attacks[0]}, 2: {gotron_attacks[1]}, "
                    f"3: {gotron_attacks[2]}, 4: {gotron_attacks[3]}]")
    if choice2 == "1":
        return print("Your OG Gotron uses Kick!")
    elif choice2 == "2":
        return print("Your OG Gotron uses Protect!")
    elif choice2 == "3":
        return print("Your OG Gotron uses Stare Down!")
    elif choice2 == "4":
        return print("Your OG Gotron uses Combustion!")
    else:
        return print("That's not a valid option. Try again."), pick_attack()


def make_sure():
    choice_run = input("Are you sure you want to run away? It's fine, there are no rewards. [Y: yes, N: no]")
    if choice_run == "y":
        return print("You ran away. Your multiplier has not been reset, bc there's no such thing.")
    elif choice_run == "n":
        return print("AttaMorty!"), take_input()
    else:
        return print("That's not a valid input. Enter y or n!")
    

def duel_prep(morty_a, morty_b):
    if morty_a.spd > morty_b.spd:
        first = morty_a
    elif morty_b.spd > morty_a.spd:
        first = morty_b
    elif Fortuna.percent_true(50):
        first = morty_a
    else:
        first = morty_b
    return morty_a.spd, morty_b.spd, first


def combat_prep(team_a, team_b):
    if team_a[0].spd > team_b[0].spd:
        first = team_a[0]
    elif team_b[0].spd > team_a[0].spd:
        first = team_b[0]
    elif Fortuna.percent_true(50):
        first = team_a[0]
    else:
        first = team_b[0]
    return team_a[0].spd, team_b[0].spd, first.name


if __name__ == '__main__':
    # random_teams = roll_teams()
    # print(random_teams)
    # initiative = combat_prep(random_teams[0], random_teams[1])
    # print(initiative)
    # random_OG_Gotron = OGGotron()
    # random_OG_Gotron2 = OGGotron()
    # print(random_OG_Gotron)
    # print(random_OG_Gotron2)
    # initiative = duel_prep(random_OG_Gotron, random_OG_Gotron2)
    # print(initiative)
    take_input()

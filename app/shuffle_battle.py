import random

from Fortuna import percent_true

from base_mortys import *


def get_player_names():
    player_1_name = input("Enter your name, player 1: ")
    # build in failsafe against malicious inputs
    player_2_name = input("Enter your name, player 2: ")
    if player_1_name and player_2_name:
        print(f"{player_1_name} is challenged by {player_2_name}!")
        return player_1_name, player_2_name
    else:
        return "You must enter names to get started."
    # can't trigger this ^ else. Instead errors: ValueError: too many values to unpack (expected 2)


def flip_a_coin(player_1_name, player_2_name):
    if percent_true(50):
        won_coin_flip = player_1_name
        lost_coin_flip = player_2_name
    else:
        won_coin_flip = player_2_name
        lost_coin_flip = player_1_name
    return won_coin_flip, lost_coin_flip


def reveal_coin_toss(player_1_name, player_2_name):
    won_coin_flip, lost_coin_flip = flip_a_coin(player_1_name, player_2_name)
    return (f"{won_coin_flip} won the coin toss! {won_coin_flip} picks 1st, 4th, 6th, 8th, and 10th. "
            f"They will win all speed ties! \n{lost_coin_flip} will pick 2nd, 3rd, 5th, 7th, and 9th.",
            won_coin_flip, lost_coin_flip)


def roll_draft_teams():
    random_mortymorty = Morty()
    random_gotron = Gotron()
    random_og_gotron = OGGotron()
    random_s4 = SeasonFour()
    random_cubism = Cubism()
    random_dragon = Dragon()
    random_fan = FanDancer()
    random_wasp = Wasp()
    random_ss = SuperSoldier()
    random_glock = Glockenspiel()

    morty_pool = [random_mortymorty, random_gotron, random_og_gotron, random_s4, random_cubism,
                  random_dragon, random_fan, random_wasp, random_ss, random_glock]
    random.shuffle(morty_pool)
    draft_pool = zip(range(1, 11), morty_pool)

    return draft_pool


def pick_a_morty(won_coin_flip, lost_coin_flip, draft_pool):
    team_a = []
    team_b = []
    pick = input(f"{won_coin_flip}, pick your first Morty (by number): ")
    if pick == "1":
        team_a.append(next(draft_pool))
        # oops, can't slice a zip??
    else:
        print("Limited Functionality: Pick #1 for now plz")
    pick2 = input(f"{lost_coin_flip}, pick your first Morty (by number): ")
    if pick2 == "2":
        team_b.append(next(draft_pool))
    else:
        print("Limited Functionality: Pick #2 for now plz")
    return team_a, team_b


if __name__ == '__main__':
    player_1, player_2 = get_player_names()
    results, winner, loser = reveal_coin_toss(player_1, player_2)
    print(results)
    print("\nBehold the Mortys!")
    roll_the_mortys = roll_draft_teams()
    print(*roll_the_mortys)
    print(pick_a_morty(winner, loser, draft_pool=roll_the_mortys))
    # i'm giving it these ^ as parameters for its inputs

import random
from base_mortys import *
# from Fortuna import percent_true
# from morty_db import *


class RandomTeams:
    def __init__(self, teams=None):
        self.teams = teams or roll_teams()

    def __str__(self):
        return f"\nTeam A is: {self.teams[0]} \n\nTeam B is: {self.teams[1]}"

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return self.teams[item]


def roll_teams():
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

    team_a = morty_pool[:5]
    team_b = morty_pool[5:]

    return team_a, team_b


def pick_a_winner(morty_a, morty_b):
    if morty_a.hp != morty_b.hp:
        winner = max(morty_a, morty_b)
        loser = min(morty_a, morty_b)
    else:
        return f"\n{morty_a.name} draws {morty_b.name}, {morty_a.hp}:{morty_b.hp}!"

    return f"\n{winner.name} defeats {loser.name}, {winner.hp}:{loser.hp}!"


def morty_war(team_a, team_b):
    """this is scratch code, obviously violates DRY. Not sure how useful it is to clean up"""
    count_a = 0
    count_b = 0
    battle_1 = pick_a_winner(team_a[0], team_b[0])
    if team_a[0].hp > team_b[0].hp:
        count_a += 1
    elif team_b[0].hp > team_a[0].hp:
        count_b += 1
    battle_2 = pick_a_winner(team_a[1], team_b[1])
    if team_a[1].hp > team_b[1].hp:
        count_a += 1
    elif team_b[1].hp > team_a[1].hp:
        count_b += 1
    battle_3 = pick_a_winner(team_a[2], team_b[2])
    if team_a[2].hp > team_b[2].hp:
        count_a += 1
    elif team_b[2].hp > team_a[2].hp:
        count_b += 1
    battle_4 = pick_a_winner(team_a[3], team_b[3])
    if team_a[3].hp > team_b[3].hp:
        count_a += 1
    elif team_b[3].hp > team_a[3].hp:
        count_b += 1
    battle_5 = pick_a_winner(team_a[4], team_b[4])
    if team_a[4].hp > team_b[4].hp:
        count_a += 1
    elif team_b[4].hp > team_a[4].hp:
        count_b += 1

    if count_a == count_b:
        return f"{battle_1} {battle_2} {battle_3} {battle_4} {battle_5} \nIt\'s a {count_a}:{count_b} draw!"
    elif count_a > count_b:
        winner_name = "Team A"
        loser_name = "Team B"
    else:
        winner_name = "Team B"
        loser_name = "Team A"

    return f"{battle_1} {battle_2} {battle_3} {battle_4} {battle_5} \n{winner_name} defeats {loser_name}, " \
           f"{max(count_a, count_b)}:{min(count_a, count_b)}!"


if __name__ == '__main__':
    random_teams = RandomTeams()
    print(random_teams)
    # random_winner = pick_a_winner(random_teams[0][0], random_teams[1][0])
    # print(random_winner)
    random_war = morty_war(random_teams[0], random_teams[1])
    print(random_war)

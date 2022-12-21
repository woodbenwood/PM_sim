from shuffle_battle import *


def pick_a_morty():
    team_a = []
    team_b = []
    pick_pool = roll_draft_teams()
    pick = input(f"{won_coin_flip}, pick your first Morty (by number): ")
    # this is erroring here ^ now anyway
    if pick == 1:
        team_a.append(pick_pool[0])
        # oops, can't slice a zip??
    else:
        print("Limited Functionality: Pick #1 for now plz")
    pick2 = input(f"{lost_coin_flip}, pick your first Morty (by number): ")
    if pick2 == 2:
        team_b.append(pick_pool[1])
    else:
        print("Limited Functionality: Pick #2 for now plz")
    return team_a, team_b


if __name__ == '__main__':
    player_1, player_2 = get_player_names()
    print(flip_a_coin(player_1, player_2))
    print("\nBehold the Mortys!")
    roll_the_mortys = roll_draft_teams()
    print(*roll_the_mortys)
    print(pick_a_morty())

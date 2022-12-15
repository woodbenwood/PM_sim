"""
Assumptions for earliest simulation playtesting purposes:
- all Mortys are max level (100) and fully trained (have max Effort Values)
- disobeying isn't a thing (Ricks/trainers are max level (50))
- if we can't randomize IV's (Inherent Values,) set to max (16) but rn we can(?)
- buffs/debuffs assumed to be 0 for now (implementation tbd)
- no perfect sim goes w/o poison and paralyze either, but this is no perfect sim (yet)
"""

import Fortuna

from app.base_mortys import OG_Gotron, Cubism, Wasp
from app.attacks import kick, erase, nibble


def percent_to_hit(acc: int) -> float:
    # ladies and gentlemen, my top-down design to turn an int into a float.
    # Needs to pull acc from attack subclass
    to_hit = acc
    return float(to_hit)


def hit_or_miss(truth_factor, roll: float) -> bool:
    truth_factor = percent_to_hit
    result = Fortuna.percent_true(truth_factor=truth_factor)
    return result


class CombatUnit:

    def __init__(self, name, team_a, team_b):
        self.name = name
        self.team_a = team_a
        self.team_b = team_b
        # show the "home" team as team_a, the opp's team as team_b


def combat_prep(team_a, team_b):
    first = max(team_a(Morty_1(spd)), team_b(Morty_1(spd)))
    # in the case of a tie, it's a coin flip
    last = min(team_a(Morty_1(spd)), team_b(Morty_1(spd)))
    # TODO fix BUG: if tied, the coin flip could make the same Morty first AND last.


def combat_turn(first, last):
    # needs to take input from both players, their choice of attack (randomize opp's if simmed)
    first(atk)
    # ugh too complicated. going to start with a duel


def random_duel(morty_1: RandomMorty, morty_2: RandomMorty):
    first = max((morty_1(spd)), (morty_2(spd)))
    # ultimately takes input: players' choice of attack (randomize opp's if simmed)
    attack = RandomMorty(proto_attack)
    if morty_1(spd) == first:
        attack.morty_1(atk)


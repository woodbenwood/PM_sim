from Fortuna import random_range


"""
Assumptions for earliest simulation playtesting purposes:
- all Mortys are max level (100) and fully trained (have max Effort Values)
- disobeying isn't a thing (Ricks/trainers are max level (50))
- if we can't randomize IV's (Inherent Values,) set to max (16) but rn we can
- buffs/debuffs assumed to be 0 for now (implementation tbd)
- no perfect sim goes w/o poison and paralyze either, but this is no perfect sim (yet)
- Fortuna's random_range is higher number exclusive, hence the +1 to each max stat.
- For min stats pre-ivs, an iv of 0 is assumed, which is impossible but temporary
"""


class Morty:
    atk_default = 251
    defense_default = 251
    spd_default = 241
    hp_default = 356
    name = "Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None):
        # self.name = "Morty"
        self.atk_iv = random_range(1, 17)
        self.defense_iv = random_range(1, 17)
        self.spd_iv = random_range(1, 17)
        self.hp_iv = (self.atk_iv + self.defense_iv + self.spd_iv) // 3
        self.atk = self.atk_default + self.atk_iv * 2 or self.atk_default
        self.defense = self.defense_default + self.defense_iv * 2 or self.defense_default
        self.spd = self.spd_default + self.spd_iv * 2 or self.spd_default
        self.hp = self.hp_default + self.hp_iv * 2 or self.hp_default

    def __gt__(self, other):
        return self.hp > other.hp

    def __repr__(self):
        output = (
            f"\n{self.name}:",
            f"HP(iv): {self.hp} ({self.hp_iv})",
            f"atk: {self.atk} ({self.atk_iv})",
            f"def: {self.defense} ({self.defense_iv})",
            f"spd: {self.spd} ({self.spd_iv})"
        )
        return "\n".join(output)


class Gotron(Morty):
    def __init__(self, atk=311, defense=321, spd=391, hp=426):
        super().__init__(atk, defense, spd, hp)
        self.name = "Gotron Morty"
        self.trivia = "I got nerfed!"


class OGGotron(Gotron):
    def __init__(self, atk=351, defense=341):
        super().__init__(atk, defense)
        self.name = "OG Gotron Morty"
        self.trivia = "The Gotron Morty before it was nerfed, a real collector's item"


class Cubism(Morty):
    def __init__(self, atk=321, defense=321, spd=331, hp=456):
        super().__init__(atk, defense, spd, hp)
        self.name = "Cubism Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd


class SeasonFour(Morty):
    def __init__(self, atk=341, defense=351, spd=301, hp=426):
        super().__init__(atk, defense, spd, hp)
        self.name = "Season 4 Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd


class Dragon(Morty):
    def __init__(self, atk=371, defense=381, spd=331, hp=436):
        super().__init__(atk, defense, spd, hp)
        self.name = "Dragon Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd


class FanDancer(Morty):
    def __init__(self, atk=271, defense=281, spd=331, hp=416):
        super().__init__(atk, defense, spd, hp)
        self.name = "Fan Dancer Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd


class Wasp(Morty):
    def __init__(self, atk=331, defense=291, spd=331, hp=396):
        super().__init__(atk, defense, spd, hp)
        self.name = "Wasp Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd


class SuperSoldier(Morty):
    def __init__(self, atk=321, defense=361, spd=321, hp=456):
        super().__init__(atk, defense, spd, hp)
        self.name = "Super Soldier Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd


class Glockenspiel(Morty):
    def __init__(self, atk=301, defense=331, spd=311, hp=416):
        super().__init__(atk, defense, spd, hp)
        self.name = "Glockenspiel Morty"
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd

# Notes from Robert following the problematic Inheritance question in OH:
# extract name, define as constant
# use two different classes, one for default, one for the randomized, maybe it's good for a third that's customizable


if __name__ == '__main__':
    random_MortyMorty = Morty()
    random_Gotron = Gotron()
    random_OG_Gotron = OGGotron()
    random_S4 = SeasonFour()
    random_Cubism = Cubism()
    random_Dragon = Dragon()
    random_FanDancer = FanDancer()
    random_Wasp = Wasp()
    random_SS = SuperSoldier()
    random_Glock = Glockenspiel()
    print(random_MortyMorty)
    print(random_Gotron)
    print(random_OG_Gotron)
    print(random_S4)
    print(random_Cubism)
    print(random_Dragon)
    print(random_FanDancer)
    print(random_Wasp)
    print(random_SS)
    print(random_Glock)

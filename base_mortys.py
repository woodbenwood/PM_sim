from Fortuna import random_range


"""
Assumptions for earliest simulation playtesting purposes:
- all Mortys are max level (100) and fully trained (have max Effort Values)
- disobeying isn't a thing (Ricks/trainers are max level (50))
- buffs/debuffs assumed to be 0 for now (implementation tbd)
- no perfect sim goes w/o poison and paralyze either, but this is no perfect sim (yet)
- Fortuna's random_range is higher number exclusive, hence range of iv's is 1-17
- For min stats pre-ivs, an iv of 0 is assumed, which is impossible but temporary
"""


class Morty:
    atk_default = 251
    def_default = 251
    spd_default = 241
    hp_default = 356
    name = "Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        self.atk_iv = random_range(1, 17) or atk_iv
        self.def_iv = random_range(1, 17) or def_iv
        self.spd_iv = random_range(1, 17) or spd_iv
        self.hp_iv = (self.atk_iv + self.def_iv + self.spd_iv) // 3 or hp_iv
        self.atk = self.atk_default + self.atk_iv * 2 or self.atk_default or atk
        self.defense = self.def_default + self.def_iv * 2 or self.def_default or defense
        self.spd = self.spd_default + self.spd_iv * 2 or self.spd_default or spd
        self.hp = self.hp_default + self.hp_iv * 2 or self.hp_default or hp
        # not sure 3 'or' options is relevant ... but will await clarity and preserve for posterity

    def __gt__(self, other):
        return self.hp > other.hp

    def __repr__(self):
        output = (
            f"\n{self.name}:",
            f"HP(iv): {self.hp} ({self.hp_iv})",
            f"atk: {self.atk} ({self.atk_iv})",
            f"def: {self.defense} ({self.def_iv})",
            f"spd: {self.spd} ({self.spd_iv})"
        )
        return "\n".join(output)


class Gotron(Morty):
    atk_default = 311
    def_default = 321
    spd_default = 391
    hp_default = 426
    name = "Gotron Morty"
    trivia = "I got nerfed!"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class OGGotron(Gotron):
    atk_default = 351
    def_default = 341
    name = "OG Gotron Morty"
    trivia = "The Gotron Morty before it was nerfed, a real collector's item"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class Cubism(Morty):
    atk_default = 321
    def_default = 321
    spd_default = 331
    hp_default = 456
    name = "Cubism Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class SeasonFour(Morty):
    atk_default = 341
    def_default = 351
    spd_default = 301
    hp_default = 426
    name = "Season 4 Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class Dragon(Morty):
    atk_default = 371
    def_default = 381
    spd_default = 331
    hp_default = 436
    name = "Dragon Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class FanDancer(Morty):
    atk_default = 271
    def_default = 281
    spd_default = 331
    hp_default = 416
    name = "Fan Dancer Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class Wasp(Morty):
    atk_default = 331
    def_default = 291
    spd_default = 331
    hp_default = 396
    name = "Wasp Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class SuperSoldier(Morty):
    atk_default = 321
    def_default = 361
    spd_default = 321
    hp_default = 456
    name = "Super Soldier Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


class Glockenspiel(Morty):
    atk_default = 301
    def_default = 331
    spd_default = 311
    hp_default = 416
    name = "Glockenspiel Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None):
        super().__init__(atk, defense, spd, hp, atk_iv, def_iv, spd_iv, hp_iv)


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

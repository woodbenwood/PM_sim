from Fortuna import random_range

"""For sake of simplicity, will only implement into main Morty parent class."""


class Morty:
    atk_default = 95
    def_default = 95
    spd_default = 85
    hp_default = 200
    name = "Morty"

    def __init__(self, atk=None, defense=None, spd=None, hp=None, atk_iv=None, def_iv=None, spd_iv=None, hp_iv=None,
                 evs=None, hp_evs=None, atk_evs=None, def_evs=None, spd_evs=None):
        self.atk_iv = random_range(1, 17) or atk_iv
        self.def_iv = random_range(1, 17) or def_iv
        self.spd_iv = random_range(1, 17) or spd_iv
        self.hp_iv = (self.atk_iv + self.def_iv + self.spd_iv) // 3 or hp_iv
        self.evs = random_range(0, 65535) or evs
        self.hp_evs = self.evs // 520 or hp_evs
        self.atk_evs = self.evs // 520 or atk_evs
        self.def_evs = self.evs // 520 or def_evs
        self.spd_evs = self.evs // 520 or spd_evs
        self.atk = self.atk_default + self.atk_evs + self.atk_iv * 2 or self.atk_default or atk
        self.defense = self.def_default + self.def_evs + self.def_iv * 2 or self.def_default or defense
        self.spd = self.spd_default + self.spd_evs + self.spd_iv * 2 or self.spd_default or spd
        self.hp = self.hp_default + self.hp_evs + self.hp_iv * 2 or self.hp_default or hp
        # not sure 3 'or' options is relevant ... but will await clarity and preserve for posterity

    def __gt__(self, other):
        return self.hp > other.hp

    def __repr__(self):
        output = (
            f"\n{self.name}:",
            "(stat) (evs) (iv)",
            f"HP: {self.hp} ({self.hp_evs}) ({self.hp_iv})",
            f"atk: {self.atk} ({self.atk_evs}) ({self.atk_iv})",
            f"def: {self.defense} ({self.def_evs}) ({self.def_iv})",
            f"spd: {self.spd} ({self.spd_evs}) ({self.spd_iv})"
        )
        return "\n".join(output)


if __name__ == '__main__':
    random_MortyMorty = Morty()
    print(random_MortyMorty)

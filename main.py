import random
from base_mortys import *
from Fortuna import random_range


"""
def random_list():
    return random.choice((random_gotron, random_cubism, random_s4, random_dragon, random_fan,
                          random_wasp, random_ss, random_glock, random_mortymorty, random_oggotron))
    # Fortuna.random_value does the same thing as random.choice
    # (RandomValue is for dependency injection specifying your own algorithm)


class RandomMorty:

    def __init__(self, morty_type=random_list()):
        self.morty_type = morty_type

    # def selection(self):
    #     self.morty_type = self.morty_type
    #     return self.morty_type

    def __str__(self):
        return f"The randomized Morty is a {self.morty_type} Morty!"

    def __repr__(self):
        return str(self)
"""


def make_random_teams():
    team_a = []
    team_b = []

    random_gotron = Gotron(
        hp=random_range(428, 458 + 1, 2),
        atk=random_range(313, 343 + 1, 2),
        defense=random_range(323, 353 + 1, 2),
        spd=random_range(393, 423 + 1, 2)
    )  # inputs ^^ needed for randomized stats
    random_cubism = Cubism(
        hp=random_range(458, 488 + 1, 2),
        atk=random_range(323, 353 + 1, 2),
        defense=random_range(323, 353 + 1, 2),
        spd=random_range(333, 363 + 1, 2)
    )
    random_s4 = SeasonFour(
        hp=random_range(428, 458 + 1, 2),
        atk=random_range(343, 373 + 1, 2),
        defense=random_range(353, 383 + 1, 2),
        spd=random_range(303, 333 + 1, 2)
    )
    random_dragon = Dragon(
        hp=random_range(438, 468 + 1, 2),
        atk=random_range(373, 403 + 1, 2),
        defense=random_range(383, 413 + 1, 2),
        spd=random_range(333, 363 + 1, 2)
    )
    random_fan = FanDancer(
        hp=random_range(418, 448 + 1, 2),
        atk=random_range(273, 303 + 1, 2),
        defense=random_range(283, 313 + 1, 2),
        spd=random_range(333, 363 + 1, 2)
    )
    random_wasp = Wasp(
        hp=random_range(398, 428 + 1, 2),
        atk=random_range(333, 363 + 1, 2),
        defense=random_range(293, 323 + 1, 2),
        spd=random_range(333, 363 + 1, 2)
    )
    random_ss = SuperSoldier(
        hp=random_range(458, 488 + 1, 2),
        atk=random_range(323, 353 + 1, 2),
        defense=random_range(363, 393 + 1, 2),
        spd=random_range(323, 353 + 1, 2)
    )
    random_glock = Glockenspiel(
        hp=random_range(418, 448 + 1, 2),
        atk=random_range(303, 333 + 1, 2),
        defense=random_range(333, 363 + 1, 2),
        spd=random_range(313, 343 + 1, 2),
    )
    random_mortymorty = MortyMorty(
        hp=random_range(328, 358 + 1, 2),
        atk=random_range(223, 253 + 1, 2),
        defense=random_range(223, 253 + 1, 2),
        spd=random_range(213, 243 + 1, 2)
    )
    random_oggotron = Gotron(
        atk=random_range(353, 383 + 1, 2),
        defense=random_range(343, 373 + 1, 2)
    )

    pool = [random_gotron, random_cubism, random_s4, random_dragon, random_fan,
            random_wasp, random_ss, random_glock, random_mortymorty, random_oggotron]

    random.shuffle(pool)  # a destructive shuffle, doesn't return anything (works like .sort not sorted())

    for i in range(len(pool)):
        if i % 2 == 0:
            team_a.append(pool[i])
        else:
            team_b.append(pool[i])

    return team_a, team_b


class RandomTeams:
    def __init__(self, teams=make_random_teams()):
        self.teams = teams

    def __str__(self):
        return f"Team A is: {self.teams[0]}! \nTeam B is: {self.teams[1]}!"

    def __repr__(self):
        return str(self)


# def make_random_og():
#     random_og = Gotron(
#         atk=random_range(353, 383 + 1, 2),
#         defense=random_range(343, 373 + 1, 2)
#     )


class RandomOGGotron:
    def __init__(self):

        self.random_og = Gotron(
            hp=random_range(428, 458 + 1, 2),
            atk=random_range(353, 383 + 1, 2),
            defense=random_range(343, 373 + 1, 2),
            spd=random_range(393, 423 + 1, 2)
        )

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    # print(dir(RandomMorty()))
    # print(RandomMorty())
    # ^^ currently not working and commented out at top
    # print(RandomTeams().__str__())
    # ^^ prints same as vv
    random_teams = RandomTeams()
    # Note to self: must use invoking "()" on the instantiation of the class, not the definition
    print(random_teams)
    # random_teams.teams[0][0].name drills down into individual stats
    # random_oggotron = RandomOGGotron()
    # print(random_oggotron.random_og)
    # ^^ these 2 lines do what this line does vv
    print(RandomOGGotron().__str__())

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
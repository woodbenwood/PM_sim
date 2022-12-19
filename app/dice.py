from base_mortys import Morty
from Fortuna import random_range

if __name__ == '__main__':
    def test_it():
        random_mortymorty = Morty()
        return random_mortymorty


def d(sides: int) -> int:
    return random_range(1, sides, 1)


def dice(rolls: int, sides: int) -> int:
    return sum(d(sides) for _ in range(rolls))


print(d(5))
print(d(7))
print(d(9))
print(d(4))
print(test_it())


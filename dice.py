from base_mortys import RandomMorty

if __name__ == '__main__':
    def test_it():
        test = RandomMorty
        return test


def d(sides: int) -> int:
    return random_range(1, sides, 1)


def dice(rolls: int, sides: int) -> int:
    return sum(d(sides) for _ in range(rolls))


print(d(9))
print(d(9))
print(d(9))
print(d(9))
print(test_it())
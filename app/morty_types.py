"""this file pre-dates the Mortys built in base_mortys, was mostly a copy paste of monster_types

MortyType = Literal[
    "Rock", "Paper", "Scissors",
]

class MortyQuery(BaseModel):
    morty_name: Optional[ShortString]
    morty_type: Optional[MortyType]
    #this is all as Robert has it in Prototype incl: challenge_rating: Optional[MonsterCR]
    #a substitute for class variable challenge_rating is in order

class RandomMorty:

    def __init__(self, morty_query: MortyQuery):

if __name__ == '__main__':
    morty = RandomMorty(MortyQuery) #a substitute for parameter challenge_rating is in order

"""
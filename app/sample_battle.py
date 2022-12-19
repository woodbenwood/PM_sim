from app.sim import take_input
from sim import *
from base_mortys import OGGotron





if __name__ == '__main__':
    player_1 = OGGotron()
    foe = OGGotron()
    print(f"You are a: {player_1}! Your foe is a {foe}!")
    take_input()

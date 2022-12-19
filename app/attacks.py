import Fortuna
from Fortuna import random_range, percent_true, truth_factor


class Attack:
    def __init__(self, name, rps_type, power, acc, ap):
        self.name = name
        self.rps_type = rps_type
        # stands for Rock, Paper, Scissors, (and N for Normal is none of these)
        self.power = power
        self.acc = acc
        self.ap = ap

    """rn doesn't mean anything to be rock/paper etc"""

    def kick(self, rps_type="rock", power=60, acc=95, ap=10):
        self.name = "Kick"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)

    def erase(self, rps_type="paper", power=70, acc=95, ap=8):
        self.name = "Erase"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)

    def nibble(self, rps_type="scissors", power=45, acc=95, ap=10):
        self.name = "Nibble"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)

    def flail(self, rps_type="normal", power=65, acc=95, ap=10):
        self.name = "Flail"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)

    def slumber(self, rps_type="rock", power=45, acc=95, ap=12):
        self.name = "Slumber"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)

    def clarity(self, rps_type="scissors", power=70, acc=95, ap=10):
        self.name = "Clarity"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)

    def hug(self, rps_type="paper", power=55, acc=95, ap=12):
        self.name = "Hug"
        self.rps_type = rps_type
        self.power = power
        self.acc = acc
        self.ap = ap
        return hit_or_miss(acc)


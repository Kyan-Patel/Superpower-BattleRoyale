from SuperPower import SuperPower

class Villain(SuperPower):
    def getStats(self):
        return self.durability + self.power + self.combat

    def getBonus(self):
        bonus = 0
        if self.intelligence > 90:
            bonus += 10
        if self.combat > 70:
            bonus += 15
        return bonus

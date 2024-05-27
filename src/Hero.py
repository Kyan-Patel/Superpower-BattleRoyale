from SuperPower import SuperPower

class Hero(SuperPower):
    def getStats(self):
        return self.intelligence + self.strength + self.speed

    def getBonus(self):
        bonus = 0
        if self.intelligence > 90:
            bonus += 10
        if self.combat < 70:
            bonus -= 15
        return bonus

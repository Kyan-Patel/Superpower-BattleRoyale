from Hero import Hero

class NonHumanHero(Hero):
    def getBonus(self):
        bonus = super().getBonus()
        if self._race != "Human":
            bonus -= 10
        return bonus

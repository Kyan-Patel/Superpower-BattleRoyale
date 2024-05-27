from Villain import Villain

class RedHairedVillain(Villain):
    def getBonus(self):
        bonus = super().getBonus()
        if self._hair_color == "Red":
            bonus += 10
        return bonus

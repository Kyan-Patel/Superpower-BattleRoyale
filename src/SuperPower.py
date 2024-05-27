class SuperPower:
    def __init__(self, name, intelligence, strength, speed, durability, power, combat, race="", hair_color=""):
        self._name = name
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.durability = durability
        self.power = power
        self.combat = combat
        self._race = race
        self._hair_color = hair_color

    # Property decorators for encapsulation
    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        if isinstance(value, int) and 0 <= value <= 105:
            self._intelligence = value
        else:
            raise ValueError("Intelligence must be an integer between 0 and 105")

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if isinstance(value, int) and 0 <= value <= 105:
            self._strength = value
        else:
            raise ValueError("Strength must be an integer between 0 and 105")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if isinstance(value, int) and 0 <= value <= 105:
            self._speed = value
        else:
            raise ValueError("Speed must be an integer between 0 and 105")

    @property
    def durability(self):
        return self._durability

    @durability.setter
    def durability(self, value):
        if isinstance(value, int) and 0 <= value <= 105:
            self._durability = value
        else:
            raise ValueError("Durability must be an integer between 0 and 105")

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if isinstance(value, int) and 0 <= value <= 105:
            self._power = value
        else:
            raise ValueError("Power must be an integer between 0 and 105")

    @property
    def combat(self):
        return self._combat

    @combat.setter
    def combat(self, value):
        if isinstance(value, int) and 0 <= value <= 105:
            self._combat = value
        else:
            raise ValueError("Combat must be an integer between 0 and 105")

    def getStats(self):
        raise NotImplementedError("Subclasses should implement this!")

    def getBonus(self):
        raise NotImplementedError("Subclasses should implement this!")

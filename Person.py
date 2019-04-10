class Person:

    def __init__(self, health, mana, damage=0):
        self._health = health
        self._mana = mana
        self._max_health = health
        self._damage = damage
    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        if self._health < 0:
            return False
        else:
            return True

    def can_cast(self):
        if self._mana < 0:
            return False
        else:
            return True

    def take_damage(self, damage_points):
        if damage_points > self._health:
            self._health = 0
        else:
            self._health = self._health - damage_points

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False
        else:
            if healing_points + self._health > self._max_health:
                self._health = self._max_health
                return True
            else:
                self._health = self._health + healing_points
                return True

    def take_mana(self, mana_points):
        self._mana += mana_points

    def attack(self, by=None):
        pass
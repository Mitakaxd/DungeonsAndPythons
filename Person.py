class Person:
    current_weapon=None
    current_spell=None

    def __init__(self, health, mana):
        self._health = health
        self._mana = mana
        self._max_health = health
    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        if self._health <= 0:
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

    def equip(Weapon weapon):
        self.current_weapon=weapon

    def learn(Spell spell):
        self.current_spell=spell

    def attack(self, by=None):
        if self.current_spell==None or self.current_weapon==None:
            return 0
        else:
            if(by=="weapon"):
                return self.current_weapon.damage
            if(by=="spell"):
                return self.current_spell.damage
